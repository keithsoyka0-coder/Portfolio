**SAMPLE — fictional client (Los Pollos Hermanos), illustrative only.**

# Page Contract — Home

**1. Page:** Home · `/` · `home`

**2. Purpose:** First impression and triage — a visitor understands what Los Pollos Hermanos is and where to go next within 10 seconds, and the brand reads legitimate and appetizing (brief §2, goal 1).

**3. Audience:** First-time visitors arriving from social or maps on mobile; potential catering clients deciding whether this business is worth a quote request.

**4. Connected features:** Catering CTA → Contact page (`/contact`) catering form. Featured-menu teaser → Menu page (`/menu`). Locations teaser → Locations page (`/locations`). Sticky header "Order Catering" CTA present on every page.

**5. Journey:**
- **Entry points:** direct URL, social links, maps listings, search. Also the SAMPLE banner ribbon sits at top; header nav below it.
- **Exit points:** `/menu` (via menu teaser + nav), `/locations` (via locations teaser + nav), `/contact` (via hero dual CTA, catering CTA, header button).
- **Intended lead destination:** `/contact` catering quote form — this page routes, it does not convert on its own.

**6. Functions & features (content modules, brief §4):**
1. Hero — red sunburst, tagline *"It's the chicken, man."* (script accent), dual CTA (primary: Order Catering → `/contact`; secondary: See the Menu → `/menu`).
2. Value-prop trio — family recipe, immaculate dining rooms, catering (three cards, one icon each, SVG only).
3. Featured menu teaser — 3–4 signature items pulled from the Menu data, CTA "See full menu".
4. Locations teaser — 3 location chips + "New location coming: Tucson AZ", CTA "Find a location".
5. Catering CTA band — full-width, short pitch, button → `/contact`.

**7. Data:** In: none (no visitor input on this page). Out: click-throughs to the three other pages. No PII collected, no secrets. The tagline and value props are static copy from the brief — no variables.

**8. Design:** Hero → trio → teaser → teaser → CTA band, single column on mobile; tokens: `--lph-red`, `--lph-yellow`, `--lph-cream`, `--lph-brown`, `--lph-red-dark`; components: `Header`, `Hero`, `ValuePropCard`, `TeaserCard`, `Footer` from the UI/UX package. Imagery rule: CSS/SVG only (sunburst hero, illustrated chicken badge, stripe dividers) — no photos.

**9. DI capabilities:** None on this page.

**10. States & flow:** Load (token-driven, no blocking requests) → render → all CTAs route to internal pages. No empty state (content is static). Error state: N/A beyond standard 404 behavior. Every link resolves to one of the 4 routes — the page must not dead-end.

**11. Accessibility:** WCAG 2.1 AA contrast throughout (red-on-cream and cream-on-red checked, no gradients on text). Keyboard-navigable header nav. Tagline in script font has sufficient size/weight; decorative sunburst marked aria-hidden.

**12. Responsible support:** SAMPLE banner fixed top ribbon on this page: "SAMPLE — fictional client demo, not a real business". Allergen note is not duplicated here — it lives on the Menu page, and the menu teaser links there rather than re-stating claims.

**13. Status:** draft · v0.1 · 2026-10-18 · sample-kit builder (draft), Keith to verify.

**Acceptance notes:** all 4 pages share the token set with no hardcoded colors; 360px and 1280px layouts verified, no horizontal scroll; provenance envelope on file.

---
© 2026 Keith Soyka / GestaltView · SAMPLE.
