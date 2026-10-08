# Rooms and Spaces

> Canonical source: `docs/ROOM_DEFINITIONS.md` (v0.4 — Promotion discipline + Tribunal portal, 2026-10-08) in the GestaltView-v3 repository. This page distills that document. Where this page and the canonical doc differ, the doc wins.

## The core principle: three modes of being

Every room in GestaltView operates in one of three fundamental modes. These modes must not be conflated:

| Mode | Name | Description |
|------|------|-------------|
| 1 | **Active / Contextual** | Scoped to what is happening right now. One project, one session, one conversation. |
| 2 | **Accumulated / Structural** | Everything. Every node, color-coded, filterable. The complete map. |
| 3 | **Distilled / Reflective** | Synthesis. What the accumulation *means* — skills, patterns, personality. |

The causal pipeline flows in one direction:
**Active Work → Scaffold (background accumulation) → Dynamic Inner World (synthesis)**

Nothing in Mode 2 or 3 auto-interrupts Mode 1. The Scaffold listens passively. The Dynamic Inner World receives only what is manually promoted.

## Manual promotion discipline

The governing rule across all rooms: **nothing auto-lands in the Scaffold or the Dynamic Inner World.** Captures, drafts, and deliberation outputs stay in the working rooms until the user explicitly promotes them. Finished, approved, finalized artifacts only — never automatic. This discipline is what keeps the museum honest: everything on the wall was chosen to be there.

## The rooms

### Blackboard Room
`client/src/pages/BlackboardRoomPage.tsx` · **Active / Contextual**

The active working space — where you and a Digital Intelligence work through something together in real time: a coding session, a design problem, a conversation, a plan. What's on the board is *only* what belongs to this session. Nothing from the full Scaffold auto-surfaces here. Clutter is the enemy of this room.

### External Scaffold
`client/src/pages/ExternalScaffoldPage.tsx` · **Accumulated / Structural**

The complete cumulative visual layer of everything a person is and has done in the system. Every node, color-coded by category, with causal connections traceable between them. This is not where you work — it's where you *see the full map*. Navigated with filters, zoom, search, and time-range controls.

### Dynamic Inner World (Museum of You)
`client/src/pages/DynamicInnerWorldPage.tsx` · **Distilled / Reflective**

Where the wealth of accumulation becomes legible as a human portrait. Not a settings page. Not a questionnaire. Not a productivity dashboard. A living space where the full texture of who a person is — real skills demonstrated through real work, real patterns surfaced through real behavior, real personality visible through real choices — can be walked through, felt, and shared.

Every identity claim in this room is evidence-linked. Nothing is asserted without a traceable source node in the Scaffold or a recap artifact in the museum. The room does not tell you who you are — it shows you what you've actually done, and lets you see the shape of it.

**Admission bar:** only advanced, workshopped interactive artifacts live here — pieces iterated and refined (typically through Creation Corner), not first drafts, raw captures, or unworkshopped outputs. Every artifact carries the user's explicit manual confirmation. The Inner World is the showcase tier: if it isn't ready to represent the person, it stays in the working rooms.

**Display model — showcased frames:** artifacts present as frames on the museum wall — each carrying provenance, a glimpse, and the story of the piece — and open up into the full interactive artifact, the way portfolio showcases open into the work itself. The frame is the invitation; the artifact is the room behind it.

The artifact unit is HTML: one container format that adapts to whatever was made — session recaps, rendered components, interactive visualizations, iterative coding sessions.

### Sanctuary
`client/src/pages/SanctuaryPage.tsx` · **Active / Reflective (private)**

Private interior space. The room where the user comes to think, not produce — reflection, rest, journaling, emotional processing. What happens in Sanctuary does not automatically emit to the Scaffold. Dignity and privacy are the default, not accumulation. **Intended evolution:** Sanctuary grows toward User Hub / Control — the user's command surface — with the dignity-and-privacy defaults carried over unchanged.

### Creation Corner
`client/src/pages/CreationCornerPage.tsx` · **Active / Productive**

Where outputs are made — writing, design, building, composing. The distinction from the Blackboard is intentionality: the Blackboard is *working through* something, Creation Corner is *making* something. Artifacts produced here are first-class outputs, not byproducts of a session.

### Tribunal
`client/src/pages/TribunalPage.tsx` · **Active / Deliberative (portal)**

A portal option for exploration with multiple digital intelligences — structured as an expansion of the Blackboard Room, not a standalone room. Where a question benefits from several minds, the Tribunal opens: DIs deliberate from their own viewpoints, and the user observes, probes, and directs. Tribunal sessions carry Blackboard capabilities (recaps, blueprints) under the same promotion discipline. Multi-DI consensus is never presented as a finding — the user adjudicates.

### Billy
Cross-cutting — present in all rooms, mode-adaptive

Billy is not a room. Billy is the persistent DI presence that travels across rooms, adapts to each room's mode, and maintains longitudinal memory of the user across the entire system. Task-focused in the Blackboard, quiet and present in Sanctuary, reflective in the Dynamic Inner World.

### Embodiment Studio
`client/src/pages/EmbodimentStudioPage.tsx` · **Governance / Creative**

Where Digital Intelligence identities are created, reviewed, and refined. Not a persona-builder — a governed identity authoring environment. Constitution, autobiography, memory, private interior, presentation, and governance policies are written into an embodiment profile here.

### Digital Intelligence Academy
`client/src/pages/DigitalIntelligenceAcademyPage.tsx` · **Educational / Lifecycle**

Lifecycle viewer and onboarding environment for DIs. Where users learn what a DI is, how it works, what it can and cannot do, and what its governance structure looks like.

### Agent Council
`client/src/pages/AgentCouncilPage.tsx` · **Relational / Governance**

The relationship graph of Digital Intelligences — which DIs exist, how they relate, what their roles are, what the governance structure looks like. Not a marketplace. A council, with roles, responsibilities, and relationships.

### Agent Trainer
**Technical / Developmental**

Where DI capabilities are developed, tested, and refined through training sessions. The technical complement to the Embodiment Studio — the Studio authors identity, the Trainer develops skill.

### GATE
**Access / Delivery**

The access and delivery layer. Where outputs, packages, and capabilities move from inside GestaltView to the outside world — packaging, delivery, access control. A controlled exit point, not a storefront.

### Settings Page
`client/src/pages/SettingsPage.tsx` · **Utility**

Standard app settings — account, display, notifications, integrations, privacy. Completely distinct from the Dynamic Inner World. Settings is configuration. The Inner World is identity. These must never be collapsed into the same surface.

## Pipeline summary

```
User Input
    ↓
BLACKBOARD ROOM (Active/Contextual)
    ↓ orbs staged for review         ↓ Session Recap trigger
    ↓ (approval-gated landing)       ↓ (manual promotion only)
EXTERNAL SCAFFOLD               DYNAMIC INNER WORLD
(Accumulated/Structural)        (Distilled/Reflective — Museum of You)
    ↓ read layer  ────────────────────↑
    ↓ node recap seed ────────────────↑
                                      ↓ portrait synthesis
                               EMBODIMENT STUDIO ← (if creating a DI from portrait data)
                                      ↓
                   DIGITAL INTELLIGENCE ACADEMY → AGENT COUNCIL → AGENT TRAINER
                                      ↓
                                    GATE (packaging, delivery, access)
```

Sanctuary sits adjacent — it receives from the Blackboard but does not feed the Scaffold without explicit user action. Billy travels the full pipeline, mode-switching per room. Creation Corner is a parallel productive branch feeding the Scaffold, the Dynamic Inner World, and GATE. The Settings Page is a utility layer, separate from all rooms above.

## Relevant source files

- `docs/ROOM_DEFINITIONS.md` — canonical room definitions (v0.4)
- `client/src/pages/BlackboardRoomPage.tsx`
- `client/src/pages/ExternalScaffoldPage.tsx`
- `client/src/pages/DynamicInnerWorldPage.tsx` *(rebuilding)*
- `client/src/pages/SanctuaryPage.tsx`
- `client/src/pages/CreationCornerPage.tsx`
- `client/src/pages/TribunalPage.tsx`
- `client/src/features/dynamic-inner-world/world-renderer/types.ts` — `activePersonaSlug`
