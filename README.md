# Snow Tour France

Static tour site on GitHub Pages: https://shashkist.github.io/snow-tour-france/

- `index.html` is the Snow Tour France 2026 page. Its photos are in `img/`.
- Every new tour gets its own folder: `<tour-slug>/index.html` + `<tour-slug>/img/`.
- Styles and scripts shared by all tours live in `assets/`.
- `python tools/check.py` checks the site: missing files, broken anchors, countdown format and image sizes.
- Edits come from a Telegram bot: request → AI edit on a branch → preview link → approve → merge to `main`.
- How to edit (for people and for the agent): see [AGENTS.md](AGENTS.md).
