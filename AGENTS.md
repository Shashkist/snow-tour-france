# Site editing guide (for the editing agent)

This repo is a static site served by GitHub Pages from `main` (root folder).
Live: https://shashkist.github.io/snow-tour-france/

Edits are requested in Russian by the tour organisers (Anna, Ilia) through a Telegram bot.
Each request runs on its own branch. The person sees a preview and approves it before anything reaches `main`.

## Layout

```
index.html              Snow Tour France 2026 (stays at the root: its URL is already shared)
img/                    photos for the root tour
<tour-slug>/index.html  each additional tour lives in its own folder
<tour-slug>/img/        photos for that tour
assets/css/site.css     shared styles for ALL tours (change only when asked about design)
assets/js/site.js       shared behaviour: photo lightbox + countdown
tools/check.py          validator: run it after every edit, it must print OK
DESIGN.md               design system + web-designer rules: READ IT for any visual change
```

## Golden rules

1. **Change only what was asked.** Don't rewrite text, restyle or "improve" anything nobody mentioned.
2. **Keep facts consistent across the page.** The same fact usually appears in several places. Update every one of them:
   - **Dates:** `<title>`, hero chip `📅`, the footer, booking deadlines in the text, and the `data-deadline` + `data-text` attributes on `<p class="cd">`.
   - **Prices:** hero chip `от … ₪` (= the cheapest total), the room cards (`.price`), the price tables in `#price` (participation + accommodation = total), and the notes under the tables. **Recalculate every total** and say in your summary which numbers you changed.
   - **Contacts:** organiser cards (`wa.me` links + the visible numbers) and the `#contacts` buttons.
3. **Russian text, existing tone.** Short sentences. Use «ёлочки» for quotes, `₪`/`€` after the number, and a non-breaking-space style thousands separator `4 500`.
4. **Never** add tracking scripts, external JS/CSS, forms that collect data, or links you weren't given.
5. Don't touch `assets/` unless the request is about design that should apply to every tour.

## Photos

- Incoming photos are saved by the bot into the tour's `img/` folder as `.jpg`.
- Insert them with the existing gallery markup:
  `<img data-g loading="lazy" decoding="async" src="img/<file>.jpg" alt="<short Russian description>">`
- Galleries are `<div class="strip">…</div>`. To remove a photo, delete its `<img>` tag. Delete the file too if nothing else uses it.
- The hero photo is set inline on `<header class="hero" style="background-image:…url(img/hero.jpg)">`.

## Building blocks (reuse them, don't invent new CSS)

| Block | Markup |
|---|---|
| Section | `<section id="…"><div class="wrap">…</div></section>`; add `class="band"` for a tinted background, alternating |
| Card grid | `<div class="grid"><div class="card">…</div></div>` |
| Big number card | `<div class="card"><div class="big">250 км</div><div>описание</div></div>` |
| Included / not included | `<ul class="ok"><li>…</li></ul>` / `<ul class="no">` |
| Highlight note | `<div class="warn">…</div>` |
| Feature chips | `<div class="fe"><span>🛏 1 спальня</span>…</div>` |
| Price line | `<div class="price">750 ₪ <small>с человека</small></div>` |
| Price table | `<table class="rows"><tr><td>…</td><td>…</td></tr></table>` |
| Extra activity row | `<div class="ex"><div><b style="color:var(--ink)">…</b><br><span style="color:var(--muted)">…</span></div><b>60 €</b></div>` |
| Numbered steps | `<ol class="steps"><li>…</li></ol>` |
| Buttons | `<a class="btn" href="…">…</a>`, secondary: `class="btn alt"` |
| Countdown | `<p class="cd" data-deadline="2026-11-25T23:59" data-text="… {d} дн. …"></p>` (hidden after the deadline) |

## Adding a new tour

1. Create `<tour-slug>/index.html` with a short latin slug, e.g. `georgia-2027`, by copying the root `index.html`.
2. Fix the asset paths for the subfolder: `../assets/css/site.css`, `../assets/js/site.js`. Photos go in `<tour-slug>/img/` and are referenced as `img/…`.
3. Replace all the content. Remove sections that don't apply instead of leaving placeholder text.
4. Keep the `<div id="lb"><img alt=""></div>` element before the script (the lightbox needs it).
5. Its URL will be `https://shashkist.github.io/snow-tour-france/<tour-slug>/`.
6. Only link it from other tours if you're asked to.

## Before you finish

Run `python tools/check.py` and fix everything it reports. End with a short summary **in Russian**, for a non-technical reader: what changed and where, plus every price/date you recalculated.
