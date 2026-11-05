# Design guide: the web-designer skill for the editing agent

Read this before any change to colours, sizes, layout, buttons or anything visual. Content edits (prices, dates, text) still follow `AGENTS.md`.

## Who looks at this site
- Russian-speaking people in Israel, about 90% of them **on a phone**, opening a link from WhatsApp or Instagram. Design for a **390px wide screen first**, then make sure the 980px desktop still looks fine.
- The page has one job: make them trust the tour and **write to Anna or Nicole on WhatsApp**. Every design decision serves that job.

## Design tokens: use these, don't invent new values
| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | #f4f8fc | #0b1624 | page background |
| `--ink` | #10243a | #eaf2fb | main text |
| `--muted` | #5a6b7d | #9db0c4 | secondary text, captions |
| `--card` | #fff | #13243a | cards |
| `--line` | #dbe5ef | #223852 | borders, table lines |
| `--soft` | #e6f0fb | #16304d | tinted sections (`.band`), chips, notes |
| `--accent` | #ff5a36 | same | **primary action** (book / write): orange |
| `--accent2` | #1a6dff | same | numbers, highlights, secondary links/buttons: blue |

- The site supports **dark mode** (`prefers-color-scheme`). Use the variables, never hard-coded colours, so both themes keep working. If a new colour is truly needed, add a variable in `:root` **and** in both dark-mode blocks.
- White text is only OK on `--accent`, `--accent2` or the dark hero. Never put `#fff` text on `var(--card)`.
- Fonts: the system stack only. No web fonts, no CDNs.

## Type and spacing scale
- Hero h1 `clamp(40px,10vw,76px)`; h2 `clamp(26px,5vw,38px)`; h3 20px. Body 16px/1.55. Captions 13–14px.
- **Prices and CTAs never get smaller.** `.price` stays ≥ 30px/800, `.big` ≥ 38px/800, `.btn` text ≥ 16px bold.
- Sections: `padding:44px 0`. Cards: radius 18px, padding 20px. Grid gap 14px. Buttons: radius 14px, padding 15px 26px.
- Max content width 980px (`.wrap`, 18px side padding).

## Components (reuse before creating)
`.btn` (orange primary), `.btn.alt` (outline secondary), `.card`, `.grid`, `.big`, `.price`, `.rows`, `.warn`, `.fe` chips, `.strip` gallery, `.ex` rows, `.steps`, `.band` tinted section, `.tag`, `.chips`, `.cd` countdown.
- To change how something looks everywhere, edit its class in `assets/css/site.css`. To change one instance, add a **modifier class** in site.css (e.g. `.btn.wa`). Avoid long inline `style=""` attributes.
- New components go in `site.css`, written in the same compact style, with light and dark colours via the variables.

## Rules that make a good change
1. **Contrast:** text at least 4.5:1 (3:1 for large bold text). Buttons must look like buttons: filled colour or a clear outline, not plain links.
2. **Touch targets:** at least 44px tall, with at least 8px between neighbours. On a phone, two buttons in a row either fit side by side or stack with a gap.
3. **One primary action per screen.** Orange `.btn` means "book / write". Don't make everything orange.
4. **Fixed or sticky elements** (a pinned button or menu): at most **one** on mobile. It must not cover content: add matching bottom padding to the `footer`, respect `env(safe-area-inset-bottom)`, and keep it off the hero heading. It shouldn't duplicate a button that's already visible on the same screen. Hide it on desktop if it's redundant there.
5. **No horizontal scroll** at 390px. Long words, phone numbers and prices must not overflow cards (`white-space:nowrap` only on short things).
6. **Hierarchy:** headline → key fact or price → action. If you make one thing louder, check that nothing more important became quieter.
7. **Consistency:** the same kind of thing looks the same everywhere (both WhatsApp buttons, both price cards, all section titles).
8. Don't remove or rewrite content during a design change, and don't change the copy when only the style was asked for.
9. Keep it light: no heavy animations, no autoplay, no new libraries.

## Process for every visual change (mandatory)
1. Read `assets/css/site.css` and the relevant part of the page.
2. Make the smallest change that achieves the request, reusing tokens and components.
3. **Look at the result with the `look` tool**: the changed section (`selector`) and, for anything fixed, sticky or near the top, the first phone screen. If you changed colours, also look with `dark: true`.
4. Check against the rules above: overlap, cut-off text, wrapping, contrast, alignment, spacing, consistency. If something is off, fix it and look again.
5. In your summary, say what changed visually in plain words.

If a request lists **several different ideas** (for example a pasted list of suggestions), don't do them all at once. Ask one short question about which ones to do, unless the person clearly said "do all of them".
