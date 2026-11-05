#!/usr/bin/env python3
"""Validate the static site before a preview/deploy. Prints OK or a list of problems (exit 1).

Checks every tour page (root index.html + */index.html):
  - no inline base64 images (they made the page 4.4 MB)
  - every local src/href/url() target exists
  - lightbox element and shared assets are wired
  - countdown attributes are well-formed
  - images are not absurdly large
"""
import re
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_IMG = 1_500_000  # bytes
problems = []


class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids, self.deadlines = [], set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for k in ("src", "href"):
            if a.get(k):
                self.refs.append(a[k])
        if a.get("style"):
            self.refs += re.findall(r"url\(['\"]?([^)'\"]+)", a["style"])
        if "data-deadline" in a:
            self.deadlines.append((a["data-deadline"], a.get("data-text", "")))


def local(ref):
    return not re.match(r"^(https?:|mailto:|tel:|#|data:|//)", ref)


def check_page(page: Path):
    rel = page.relative_to(ROOT)
    html = page.read_text(encoding="utf-8")
    if "base64," in html:
        problems.append(f"{rel}: inline base64 data found, save images as files in img/")
    p = Collect()
    p.feed(html)
    for ref in p.refs:
        if not local(ref):
            if ref.startswith("#") and len(ref) > 1 and ref[1:] not in p.ids:
                problems.append(f"{rel}: anchor {ref} has no matching id")
            continue
        target = (page.parent / ref.split("#")[0].split("?")[0]).resolve()
        if not target.exists():
            problems.append(f"{rel}: missing file {ref}")
        elif ROOT not in target.parents and target != ROOT:
            problems.append(f"{rel}: {ref} points outside the site")
    if "lb" not in p.ids:
        problems.append(f'{rel}: lightbox <div id="lb"><img alt=""></div> is missing')
    if not any(r.endswith("assets/css/site.css") for r in p.refs):
        problems.append(f"{rel}: shared stylesheet assets/css/site.css not linked")
    if not any(r.endswith("assets/js/site.js") for r in p.refs):
        problems.append(f"{rel}: shared script assets/js/site.js not linked")
    for dl, text in p.deadlines:
        try:
            datetime.fromisoformat(dl)
        except ValueError:
            problems.append(f"{rel}: data-deadline '{dl}' is not YYYY-MM-DDTHH:MM")
        if "{d}" not in text:
            problems.append(f"{rel}: countdown data-text must contain {{d}}")


pages = [ROOT / "index.html"] + sorted(p for p in ROOT.glob("*/index.html") if p.parent.name not in ("tools", "assets"))
for pg in pages:
    check_page(pg)
for img in ROOT.rglob("img/*"):
    if img.is_file() and img.stat().st_size > MAX_IMG:
        problems.append(f"{img.relative_to(ROOT)}: {img.stat().st_size // 1024} KB is too big (max {MAX_IMG // 1024} KB), resize it")

if problems:
    print("PROBLEMS:\n- " + "\n- ".join(problems))
    sys.exit(1)
print(f"OK ({len(pages)} page(s))")
