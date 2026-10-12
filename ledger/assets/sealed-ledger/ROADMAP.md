# Capability Ledger — Product Roadmap
_Issuer-directed; newest first._

## 1. Per-claim promotion criteria + gap breakdown (issuer, 2026-10-11)

**Issuer's words:** "Looking at each claims cited sources is exactly the micro details
a system like this should implement with strict requirements of what's enough to be
promoted to verified and a breakdown of what's there, not there, planned, pending or
just a future target which can be used for roadmap design for any user."

**Spec:**
- **Promotion criteria (strict, per grade transition):** define exactly what evidence
  is sufficient to promote a claim between grades — e.g. partial → verified requires
  named, checkable artifacts (file path / URL / log) independently confirmed; planned →
  partial requires existence evidence; any promotion requires issuer verdict. No silent
  upgrades; the criteria themselves are versioned and visible.
- **Per-claim source breakdown:** for each claim's cited sources, show five states —
  **there** (verified present), **not there** (named but unlocatable), **planned**
  (spec exists, not built), **pending** (awaiting a specific evidence event, e.g. a log
  run), **future target** (aspirational, no commitment date). The breakdown is the
  micro-detail view behind every grade badge.
- **Roadmap generation:** the gap between current sources and promotion criteria
  compiles into a per-user roadmap — "to promote C-024 to verified, supply X."
  The ledger stops being a static record and becomes the plan for strengthening itself.
- **Boundary preservation:** promotion never rewrites history — red-to-green arcs,
  exclusions, and prior grades stay on the record.

**Status:** specified, not yet built.
