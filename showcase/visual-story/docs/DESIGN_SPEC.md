# GestaltView Wiki Visual Story Layer — Design Spec

**Date:** 2026-10-07  
**Status:** Approved and implemented; see the implementation plan for verified scope and limitations  
**Source:** `GestaltView_Master_Wiki_v4.0.pdf` (116 pages)

## Goal

Create a standalone, interactive visual storytelling layer that makes the diagrams and figures in the full GestaltView wiki useful as entry points for readers with different levels of technical familiarity—from first-time visitors to architecture engineers.

The experience should explain what the visuals show without replacing their source meaning, collapsing proposed architecture into current runtime claims, or requiring readers to understand the repository before they can begin.

## Selected approach

Use a **depth-first story with a complete visual atlas**. Each visitor chooses an entry depth first; the guided story and unrestricted catalog remain available from there.

Rejected alternatives:

- A tour limited to the 13 opening diagrams would be clearer but incomplete against the user's request.
- A diagram-only reference atlas would cover more material but would not provide the requested storytelling entry points.

## Reader entry points

The start screen offers three plain-language choices:

1. **Get oriented** — everyday language, what the system is for, and why each part matters.
2. **Understand the system** — product surfaces, roles, data movement, and boundaries.
3. **Explore the architecture** — runtime, implementation relationships, evidence, and technical details.

These are lenses on shared material, not separate or contradictory versions of the system. A reader can inspect other depth levels at any time.

## Story structure

The guided path groups visuals by the questions they answer, rather than by repository directory alone:

1. Why does being seen need infrastructure?
2. How does a thought or fragment enter the system?
3. Where does it go across rooms, memory, and continuity?
4. How do Billy and collaborating Digital Intelligences participate?
5. How does work become an artifact or downstream action?
6. What governs the boundaries, evidence, and technical topology?

A searchable, browsable atlas is available alongside the guided path; visitors are not required to follow a linear tour.

## Visual and interaction model

- Present one focal diagram or figure at a time, with a concise narrative and navigation to related visuals.
- Make important nodes or regions interactive where their identity can be mapped reliably. Selecting a hotspot reveals its everyday meaning, system role, and technical/source detail at the selected depth.
- Preserve the original figure or diagram where its Mermaid source is unavailable. Do not redraw a rendered figure and imply that the reconstruction is the original source.
- Add caption, source page, and an evidence/source note to each catalog item.
- Distinguish current, planned, deprecated, and conceptual status only when the source explicitly supports that distinction.
- Keep interaction keyboard-accessible and usable on narrow screens; provide a non-interactive text explanation for every visual.

## Source inventory and extraction rules

The preliminary PDF inspection found 13 curated diagrams in the opening visual layer and at least 39 deeper figure captions. These are discovery counts, not a final verified total: captions may group multiple visuals, and each deeper figure must be checked to confirm what it depicts and whether it is in scope.

The complete 116-page PDF is the source-of-truth boundary. The older project exhibit containing 98 Mermaid blocks may be used as a comparison aid only; it must not be merged into the new artifact unless each item is verified against the PDF or a clearly cited source. For every included item, record the PDF page and caption/title where available. Track any ambiguous, unreadable, or unextractable visual in the inventory rather than silently omitting it.

Render Mermaid source when it is actually available and attributable. Where only a rendered diagram/figure is present, use the source image/page rendering and add clearly attributed explanatory interaction around it.

## Voice and claim discipline

Use GestaltView's warm, precise, lightly bureaucratic voice. Keep humor as a frame for difficult material, not a way to minimize it. Use **Digital Intelligence (DI)** in new explanatory copy. Preserve source terminology in quoted labels or reproduced diagrams when needed for fidelity, while making clear that it is source language.

Avoid describing a conceptual or planned pathway as a live capability. Explanations must separate human purpose, system behavior, and implementation evidence.

## Deliverable and constraints

- A standalone browser-openable web artifact, with no backend or external account required.
- Include the complete visual inventory and local or embedded resources needed by the experience.
- No publication, deployment, or integration into the live GestaltView application is in scope.

## Validation criteria

1. Every diagram/figure identified as in scope across the PDF is represented or explicitly listed as an extraction exception.
2. Every visual has a source page and title/caption where present.
3. Mermaid renderings are traceable to available source; reconstructed or merely explanatory overlays are visibly distinguished from source diagrams.
4. The three entry points provide materially different levels of explanation without changing system facts.
5. Guided navigation, atlas/search, hotspots, keyboard interaction, and narrow-screen layout work in a browser.
6. No unsupported status or runtime claim is introduced.

## Open implementation detail

The exact final visual inventory and the best extraction method for each item remain to be established during source-cataloging. If a visual cannot be read or mapped confidently, preserve the uncertainty in the artifact's source notes rather than infer its content.
