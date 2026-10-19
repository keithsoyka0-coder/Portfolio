# Web Sample Artifact Carousel — Design

**Status:** Proposed for implementation review. The owner approved the five-item, one-at-a-time preview carousel concept and the prior request to keep portfolio changes local with no preview deployment.

## Goal

Give visitors a useful look inside the fictional Web Discovery kit without requiring them to download the full ZIP first. Keep the existing public-safe ZIP as the complete-package download and preserve the current service terms and fictional-sample disclosures.

## Placement and contents

Add a carousel within `#web-deliverables-sample` in `services.html`. It contains these five HTML artifacts from the existing public-safe archive:

1. Discovery findings
2. Implementation specification
3. Design specification and theme package
4. Desktop home mock board
5. Mobile home and menu mock board

Each slide includes a concise title, a sandboxed iframe preview, and separate “Open full preview” and “Download HTML” links. The ZIP download remains the way to get the complete kit, including page contracts, PDFs, README, brief, and provenance manifest. The original uploaded ZIP remains untouched; public sample content continues to label the Los Pollos Hermanos scenario as fictional and unaffiliated, and the owner’s current $600 Discovery / $2,900 build terms remain clearly distinguished from fictional restaurant details. The license-key/degraded-mode mechanism stays out of public-facing files.

## Interaction and accessibility

- One slide is selected at a time; there is no autoplay.
- Previous/next buttons and a position indicator control the selected slide.
- Native horizontal scrolling and scroll snapping provide touch/swipe navigation.
- Keyboard users can operate the controls, and focus remains predictable after navigation.
- The carousel region and slides have accessible names; a polite live status announces position changes.
- Iframes use a restrictive sandbox without script permission, lazy-load, and have descriptive titles.
- Navigation respects `prefers-reduced-motion`; with JavaScript unavailable, the previews remain reachable through the horizontal scroller and the direct links.

## Implementation boundaries

- Use the existing static HTML, CSS, and JavaScript conventions; no framework or external carousel dependency.
- Extract only the five listed HTML files from the already sanitized archive into a clearly named preview directory. Do not alter the archive or expose the removed license-key instructions.
- Keep styling scoped to the carousel and responsive at phone, tablet, and desktop widths.
- Preserve existing unrelated tablet header behavior and all service-page pricing.
- Keep all changes local and uncommitted. Do not push, open a PR, publish, or deploy a preview without a new owner instruction.

## Acceptance checks

1. All five artifact titles, preview sources, and direct open/download links map to real local files.
2. The carousel changes slides with previous/next controls and touch scrolling; position status stays in sync.
3. Keyboard-only navigation and screen-reader labels/status are usable; iframe sandbox blocks scripts.
4. Reduced-motion preference avoids smooth animation; no-JavaScript scrolling and links still work.
5. At 320px, 390px, tablet, and desktop widths, the component has no new horizontal page overflow and the existing sample card/ZIP link remains intact.
6. The sanitized ZIP remains unchanged and passes integrity/provenance/disclosure checks.
7. Relevant page/archive tests and `git diff --check` pass. No remote changes or deployment occur.
