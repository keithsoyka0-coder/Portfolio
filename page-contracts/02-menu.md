**SAMPLE — fictional client (Los Pollos Hermanos), illustrative only.**

# Page Contract — Menu

**1. Page:** Menu · `/menu` · `menu`

**2. Purpose:** Show the food — appetizing, scannable, and easy to update — so a visitor can decide what to order and a catering client can reference items when requesting a quote (brief §2, goals 1–3).

**3. Audience:** Visitors checking what's on offer; catering prospects scoping a menu for an event; return visitors who want prices without asking.

**4. Connected features:** Catering CTA after each category ("Need this catered? Get a quote" → `/contact`). Nav to Home, Locations, Contact. Allergen note feeds the Contact FAQ's allergen question.

**5. Journey:**
- **Entry points:** header nav, Home hero secondary CTA, Home featured-menu teaser, search.
- **Exit points:** `/contact` (catering CTA — primary), `/locations` (nav), `/` (nav).
- **Intended lead destination:** `/contact` catering quote form — the menu's job is to make the visitor *want* to ask, not to take an order (no online ordering: out of scope, brief §3).

**6. Functions & features (content modules, brief §4):**
1. Category: **Chicken** — 8 pc. Famous Recipe $14.99, Tenders $9.99, Sandwich $8.49.
2. Category: **Sides** — Curly Fries $3.99, Slaw $2.99, Corn $2.49.
3. Category: **Drinks & Desserts** — Horchata $2.99, Flan $4.49.
4. Allergen note — plain-language statement, visually distinct (card/border), no medical claims beyond "ask staff."
5. Per-category catering CTA → `/contact`.
- All items/prices fictional. Category cards: SVG/typographic treatment, no photos.

**7. Data:** In: none (no visitor input). Out: click-throughs to `/contact`. **Editable region (brief §3, §7.4):** the menu items and prices live in ONE plainly-marked data block at the top of the page source, commented for a non-technical manager, e.g.:
```html
<!-- ═══ EDIT MENU HERE ═══
     To change an item or price, edit the text between the quotes.
     Don't touch anything else. -->
```
Adding/removing items in that block must re-render the cards with no code changes.

**8. Design:** Stacked category sections, card grid per category; tokens: `--lph-cream` page bg, white cards, `--lph-brown` body text, `--lph-orange` dividers, `--lph-yellow` price badges; components: `Header`, `MenuCategoryCard`, `CtaBand`, `Footer` from the UI/UX package. Typography: Oswald headings, Inter body.

**9. DI capabilities:** None on this page.

**10. States & flow:** Load → render all categories. Empty state: a category with zero items in the editable block renders a "Coming soon" placeholder card, never a blank gap. Error state: none expected beyond 404; malformed editable-block entries fail closed to the placeholder, not a broken layout.

**11. Accessibility:** WCAG 2.1 AA contrast; prices legible at small sizes; allergen note readable by screen readers as emphasized text (not color-only); keyboard-navigable CTAs; no price information conveyed by color alone.

**12. Responsible support:** Prices are fictional and fixed by the brief — never present them as real. Allergen note is factual and cautious: it informs, never guarantees safety. SAMPLE banner ribbon visible. No dark patterns (no fake scarcity, no "order now" urgency when ordering doesn't exist on the site).

**13. Status:** draft · v0.1 · 2026-10-18 · sample-kit builder (draft), Keith to verify.

**Acceptance notes:** menu items and prices editable in the marked region by a non-technical manager (§7.4); all colors from tokens; 360px/1280px verified; provenance envelope on file.

---
© 2026 Keith Soyka / GestaltView · SAMPLE.
