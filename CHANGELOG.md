# Changelog — Keith Soyka Portfolio Site

## v10.2 — 2026-10-02
**Conversion pass (Grok + Perplexity reviews, run through the register)**
- index.html: bridge sentence under the hero lede (consultant ↔ GestaltView founder — "I bring that same discipline to client systems"); primary CTA "Book a free 15-minute call" → "Find the real constraint" ("free" dropped from the button); new curiosity row under the hero — "Meet Billy" / "Convene the Tribunal" buttons firing straight to the live demos; Lane B card reframed (identity & communication systems, logo prices de-emphasized on the index).
- services.html: every Lane A package card is now a complete conversion unit — inclusions + explicit deliverable ("You leave with") + sample PDF link + Stripe pay button + contact link; design lane reframed ("I make complicated systems intelligible to the people who must choose, fund, use, or operate them"), logo moved to a scoped offering (last card, pay links intact); new "Who this is for — and not for" fit section; bottom CTA → "Find the real constraint".
- Bundled the v1.9 showcase demos into the tree (showcase.html with Live Demos + 5 demo pages + config/css/proxy) so this package deploys self-contained. Canonical source for the demo pages remains the showcase package (v1.9).
- styles.css: .bridge, .curiosity-label, .deliverable.

## v10.1 — 2026-09-29
**SEO gap patch (from June v2.0 audit checklist)**
- brand-sheet.html: added missing meta description, canonical URL, and OG
  tags (og:title, og:description, og:url, og:type). All 8 pages now carry
  complete per-page SEO headers.

## v10 — 2026-09-28
**Dynamic Inner World Showcase + contact retirement**
- Added `showcase.html`: gallery of 11 standalone interactive HTML artifacts
  (inner-world exhibits ×3, systems architecture map, comprehensive profile,
  Agent Trainer sprint + pricing, 4-piece Canva brand kit).
- Added `showcase/`: the 11 exhibit files with clean filenames, verified
  link-complete (30/30 links resolve, all titles intact).
- Added Showcase to header nav + footer on all pages; updated sitemap.xml,
  sitemap.txt, sitemap.html.
- Retired 646-513-6410 → (646) 741-6849 in index.html (metadata), contact.html
  (tel: link + display), brand-sheet.html (contact line). Zero occurrences remain.
- Email split confirmed (no change): keithsoyka@gestaltview.onmicrosoft.com =
  contract & advisory; keithsoyka@gmail.com = operations & general.
- Added README.md (Vercel + HuggingFace static-Space deploy notes).
- Open: portfolio "live runtime" link points at gestaltview-v3-psi (welcome
  page); gestaltview-three serves the actual runtime — awaiting Keith's call.
