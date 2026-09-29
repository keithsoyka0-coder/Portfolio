# Keith Soyka — Portfolio Site · v10

Static portfolio site for Keith Soyka (AI systems builder, founder of GestaltView).
Live: https://keith-soyka-portfolio.vercel.app/

## What's inside (v10)
- `index.html` — home
- `work.html` — selected work
- `showcase.html` — **Dynamic Inner World Showcase**: gallery of 11 standalone
  interactive HTML artifacts from the GestaltView build (inner-world exhibits,
  systems architecture map, Agent Trainer package, Canva-ready brand kit)
- `showcase/` — the 11 exhibit HTML files (self-contained, open directly)
- `services.html`, `about.html`, `contact.html`, `sitemap.html`
- `brand-sheet.html` — GestaltView brand sheet (standalone)
- `styles.css`, `script.js`, `og-image.png`, `robots.txt`, `sitemap.xml/txt`
- Resumes (PDF) + sample audit/plan PDFs

## Contact conventions (v10)
- Business phone: **(646) 741-6849** (retired 646-513-6410 in v10)
- Business email: **keithsoyka@gestaltview.onmicrosoft.com**
  (contract & advisory inquiries)
- General email: **keithsoyka@gmail.com** (operations & general inquiries)

## Deploy — Vercel (repo)
Push to the repo's `main` branch; Vercel auto-deploys the static files.
Note: `brand-sheet.html` is served from this repo — make sure it is committed
or a deploy will drop it from the live site.

## Deploy — Hugging Face Space (static)
1. Create a new Space → SDK: **Static** → visibility as desired.
2. Upload the contents of this folder (or `git push` to the Space repo).
3. The Space serves `index.html` at the root; `showcase/` exhibits open from
   the Showcase page. No build step, no secrets, no server code.

## Evidence standard
Every claim on this site is labeled by what backs it — **verified**
(artifact, test, or observation), **staged** (in build, documented), or
**planned** (intent, not yet built). Nothing here asks for trust it hasn't earned.

© 2026 Keith Soyka. Built to be inspected.
