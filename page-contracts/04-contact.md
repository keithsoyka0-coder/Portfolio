**SAMPLE — fictional client (Los Pollos Hermanos), illustrative only.**

# Page Contract — Contact

**1. Page:** Contact · `/contact` · `contact`

**2. Purpose:** The conversion page — it exists to collect **catering quote requests** and route **franchise inquiries**, the two conversions in brief §2, goal 2. Everything else on the page (FAQ, inquiry block) serves those two outcomes.

**3. Audience:** Catering prospects ready to ask for a quote (event planners, offices, families); franchise-interested visitors; visitors with one of the four FAQ questions.

**4. Connected features:** Catering form → fictional inbox delivery. Franchise inquiry block → separate email link. FAQ covers: catering minimums, franchise info, allergens, hours. Sticky header "Order Catering" CTA lands here.

**5. Journey:**
- **Entry points:** header nav, Home hero primary CTA, Home catering CTA band, Menu per-category catering CTAs, Locations catering links — nearly every page routes here; this is the site's conversion endpoint.
- **Exit points:** form success confirmation (terminal state); back to `/`, `/menu`, `/locations` via nav.
- **Intended lead destination:** form submission → confirmation. There is no deeper funnel — success is the message sent.

**6. Functions & features (content modules, brief §4):**
1. **Catering quote form** — fields: name, email, event date, guests, message. Labels above inputs, inline validation, submit → fictional inbox.
2. **Franchise inquiry block** — separate email link (visually distinct from the catering form so the two conversions don't get confused).
3. **FAQ accordion** — 4 questions: catering minimums, franchise info, allergens, hours. Accordion: keyboard-operable, one open at a time.
4. Trust line under the form: what happens next ("We'll reply within one business day" — fictional commitment, stated plainly).

**7. Data:** In: name, email, event date, guests, message (visitor input — PII). Out: form submission → fictional inbox. **No PII stored on the site**; no secrets, no keys in the package (variables rule — the inbox destination travels via trusted email attachment, and this contract describes the shape only). Event date and guest count validated as sensible values (date not in the past, guests positive integer).

**8. Design:** Two-column desktop (form left, franchise block + FAQ right), single column mobile; tokens: `--lph-cream` bg, white form card, `--lph-red` pill submit button + cream text, `--lph-orange` focus rings; components: `Header`, `ContactForm`, `FaqAccordion`, `Footer` from the UI/UX package.

**9. DI capabilities:** None on this page.

**10. States & flow (the test surface — every state must be reachable):**
1. Load → idle form, all fields empty.
2. Submit with missing/invalid fields → inline validation, error copy appears next to the field, focus moves to first error, **entered input preserved**.
3. Submit valid → sending state (button disabled, "Sending…") → success: confirmation message replaces form ("Thanks — your request is on its way."), no redirect.
4. Delivery failure → error state: nonjudgmental copy ("Something went wrong on our end — your message wasn't sent. Try again in a minute."), **input preserved**, retry button.
5. FAQ accordion: all closed by default → open on click/Enter → close on second toggle; only one open at a time.

**11. Accessibility:** Labels on all fields (above inputs, not placeholder-only); inline errors announced via aria-live; keyboard-navigable accordion (Enter/Space, arrow optional); focus-visible styles; AA contrast on error text (never red-on-red alone); form fully operable without a mouse.

**12. Responsible support:** Error copy never blames the user; no dark patterns (no pre-checked consent boxes, no hidden fields). The fictional "one business day" reply commitment is labeled as fictional in this demo. Franchise email link is a plain `mailto:`-style link — no data captured. SAMPLE banner ribbon visible.

**13. Status:** draft · v0.1 · 2026-10-18 · sample-kit builder (draft), Keith to verify.

**Acceptance notes:** keyboard-navigable form; all colors from tokens; 360px/1280px verified; provenance envelope on file. Conversion tracking (if any) is out of scope for the demo — noted, not built.

---
© 2026 Keith Soyka / GestaltView · SAMPLE.
