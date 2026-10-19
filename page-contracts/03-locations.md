**SAMPLE — fictional client (Los Pollos Hermanos), illustrative only.**

# Page Contract — Locations

**1. Page:** Locations · `/locations` · `locations`

**2. Purpose:** Answer "find us" — a visitor can pick a location, see hours/phone, and get directions without calling, so announcing a new location never requires rebuilding the site (brief §2, goal 3).

**3. Audience:** Visitors on mobile near one of the locations; people planning a visit or checking hours before a catering pickup.

**4. Connected features:** "Get directions" outbound link per location (maps). Nav to Home, Menu, Contact. Each location card optionally links catering questions → `/contact`.

**5. Journey:**
- **Entry points:** header nav, Home locations teaser, search/maps, Contact page (visitors checking where they're nearest before inquiring).
- **Exit points:** outbound maps links (external), `/contact` (nav / catering CTA), `/` (nav), `/menu` (nav).
- **Intended lead destination:** maps directions link (visit intent) or `/contact` (inquiry intent) — this page supports both, converts neither directly.

**6. Functions & features (content modules, brief §4 — all fictional):**
1. Location card × 3: **Albuquerque NM** (Central Ave — Flagship), **Santa Fe NM**, **El Paso TX** — each with fictional address, hours Mon–Sun 10am–10pm, phone, "Get directions" link.
2. "New location coming: Tucson AZ" announcement banner — visually distinct from live locations so it can't be mistaken for open.
3. Optional per-card catering link → `/contact`.
- Addresses and phone numbers are fictional; never real data.

**7. Data:** In: none. Out: outbound maps links; internal links to `/contact`. **Editable region (brief §3, §7.4):** all location entries (address, hours, phone, directions URL, and the "coming soon" line) live in ONE plainly-marked data block at the top of the page source, commented for a non-technical manager. Adding a 4th location there must add a card with no code changes. No secrets; the variables rule is trivially satisfied (no real business values exist).

**8. Design:** Card grid, one card per location, announcement banner above/below grid; tokens: `--lph-cream` bg, white location cards, `--lph-yellow` "coming soon" badge, `--lph-brown` text; components: `Header`, `LocationCard`, `AnnouncementBanner`, `Footer` from the UI/UX package.

**9. DI capabilities:** None on this page.

**10. States & flow:** Load → render all location cards + announcement. Empty state: if the editable block contains zero locations, show a single card: "New locations coming soon — check back." Error state: a directions link with a missing URL renders as plain address text, never a dead button.

**11. Accessibility:** WCAG 2.1 AA contrast; "coming soon" status conveyed by text, not color alone; phone numbers are `tel:` links with readable labels; keyboard-navigable cards and links; screen-reader order: name → address → hours → phone → directions.

**12. Responsible support:** Fictional addresses only — the contract records that no real address may ever be substituted without client sign-off. Hours stated once and consistently (Mon–Sun 10am–10pm) to avoid contradiction with the Contact FAQ. SAMPLE banner ribbon visible.

**13. Status:** draft · v0.1 · 2026-10-18 · sample-kit builder (draft), Keith to verify.

**Acceptance notes:** locations editable in the marked region by a non-technical manager (§7.4); all colors from tokens; 360px/1280px verified; provenance envelope on file.

---
© 2026 Keith Soyka / GestaltView · SAMPLE.
