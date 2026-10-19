# FICTIONAL CLIENT BRIEF — the complete spec every sample deliverable is built from

> **SAMPLE — FICTIONAL CLIENT.** Los Pollos Hermanos is a fictional restaurant chain from the TV series *Breaking Bad*. This brief is invented for demonstration purposes. No real business data. Every deliverable built from this brief must carry a visible SAMPLE banner.

## 1. Client fiction

**Los Pollos Hermanos** ("The Chicken Brothers") — a fictional family-owned fried-chicken restaurant chain, "as seen on TV." Founded by fictional brothers Gus Fring and Max Arciniega. Known for immaculate restaurants, courteous staff, and the famous curly fries. The (fictional) ask: a franchise group wants a modern 4-page marketing site to support catering inquiries and new-location announcements.

## 2. Engagement goals (the fictional "why")

1. Look legitimate and appetizing — the site is the first impression for catering clients.
2. Drive two conversions: **catering quote requests** and **franchise inquiries**.
3. Announce new locations without rebuilding the site each time (content must be editable by a non-technical manager).
4. Load fast on phones — most visitors arrive from social/maps on mobile.

## 3. Constraints (fictional)

- 4 pages only: Home, Menu, Locations, Contact.
- No online ordering, no payments, no accounts. (Out of scope — stated plainly.)
- No real photography available; use CSS/SVG illustration and typography to carry the brand.
- Must meet WCAG 2.1 AA contrast. Copy in English only.
- Handoff must be maintainable by a non-technical manager (menu items and locations editable in plainly-marked spots).

## 4. Pages & purpose

| Page | Purpose | Key content (fictional) |
|---|---|---|
| Home | First impression; sell the brand; route visitors | Hero (tagline "It's the chicken, man." — invented for this sample), 3 value props (family recipe, immaculate dining rooms, catering), featured menu teaser, locations teaser, catering CTA |
| Menu | The food, appetizing and scannable | Categories: Chicken (8 pc. Famous Recipe $14.99, Tenders $9.99, Sandwich $8.49), Sides (Curly Fries $3.99, Slaw $2.99, Corn $2.49), Drinks & Desserts (Horchata $2.99, Flan $4.49). All prices fictional. Allergen note. |
| Locations | Find us | 3 fictional locations: Albuquerque NM (Central Ave — Flagship), Santa Fe NM, El Paso TX. Each: address (fictional), hours (Mon–Sun 10am–10pm), phone, "Get directions" link. "New location coming: Tucson AZ." |
| Contact | Two conversions | Catering quote form (name, email, event date, guests, message) → fictional inbox. Franchise inquiry block (separate email link). FAQ: 4 questions (catering minimums, franchise info, allergens, hours). |

## 5. Design tokens (the theme package)

**Palette**
- `--lph-red: #B3122E` — primary brand red (headers, hero background, CTAs)
- `--lph-yellow: #FFC72C` — warm brand yellow (accents, highlights, badges)
- `--lph-cream: #FFF6E5` — page background
- `--lph-brown: #4A2C1A` — body text (dark roast brown)
- `--lph-orange: #E87722` — secondary accent (hovers, dividers)
- `--lph-red-dark: #7E0C20` — footer / deep contrast sections
- White `#FFFFFF` for cards on cream.

**Typography**
- Headings: bold condensed — `'Oswald', 'Arial Narrow', sans-serif` (Google Fonts link as progressive enhancement; system fallback required)
- Body: clean sans — `'Inter', 'Helvetica Neue', Arial, sans-serif`
- Accent/script for taglines: `'Caveat', cursive` fallback cursive (use sparingly)

**Spacing & shape**
- Base unit 8px; section padding 64px desktop / 40px mobile
- Cards: 12px radius, 1px solid rgba(74,44,26,.12), soft shadow
- Buttons: pill (999px radius), red bg + cream text; yellow variant for dark sections
- Retro diner feel: subtle diagonal-stripe or sunburst motifs allowed; no gradients on text (AA contrast)

**Imagery rule:** no photos — CSS/SVG only (sunburst hero, illustrated chicken badge, stripe dividers).

## 6. Components

Header (sticky, red, logo badge + nav + "Order Catering" CTA) · Hero (red sunburst, tagline, dual CTA) · Value-prop trio · Menu category cards · Location cards · Contact form (labels above inputs, inline validation) · FAQ accordion · Footer (red-dark, hours, fictional addresses, "SAMPLE — fictional demo" microcopy) · SAMPLE banner (fixed top ribbon on every page: "SAMPLE — fictional client demo, not a real business").

## 7. Acceptance criteria (what "done" means for the fictional build)

1. All 4 pages render from the token set above — no hardcoded colors outside tokens.
2. Mobile (360px) and desktop (1280px) layouts verified; no horizontal scroll.
3. Contrast AA on all text. Keyboard-navigable nav and form.
4. Menu items and locations editable in marked regions a non-technical manager can find.
5. Every file carries the provenance envelope line: `© 2026 Keith Soyka / GestaltView · SAMPLE`.
6. No real business data anywhere; SAMPLE banner visible on every page.

## 8. What is NOT in this kit

The actual site build (HTML/CSS/JS of the finished site) — the kit shows everything *around* the build: findings, specs, contracts, mock boards, README. That absence is the point: this is what the client sees before and after the build.
