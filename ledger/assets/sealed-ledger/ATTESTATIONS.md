# Ledger Attestations

Issuer: Keith Soyka. No AI output is ever a finding; an attestation below is the
issuer's own verdict, recorded verbatim.

## 2026-10-11 — Capability Ledger Prototype v2.0 (artifact attestation)

**Issuer statement (verbatim):** "I attest the v2 prototype"

**Scope of this attestation:** the v2.0 portal ARTIFACT itself — i.e., it faithfully
presents the ledger package contents (37 draft claims, grade distribution 25/10/2,
exclusions register, design principles, red-to-green journey records) as they stand.

**Explicitly NOT covered:** per-claim attestation. The 37 claims remain DRAFT pending
individual verdicts (attest / edit / re-grade / drop). This artifact attestation does
not upgrade any claim's grade or status.

**Claims with individual issuer verdicts so far (2026-10-11):** C-002, C-003, C-005,
C-011, C-012, C-014, C-017, C-022, C-023, C-024, C-033.

## 2026-10-11 — Full claims attestation (blanket)

**Issuer statement (verbatim):** "I attest the claims and their strict boundary controls."

**Scope:** all 37 claims (C-001–C-037) as presented in the v2.0 portal and the
ledger package, **at their current evidence grades and with their boundary controls
intact** — including the EXCLUSIONS.md register, gated revenue projections, scope
boundaries (corpus vs runtime, snapshot dates), and red-to-green journey records.

**Basis:** 11 claims received individual verdicts during the 2026-10-11 session
(C-002, C-003, C-005, C-011, C-012, C-014, C-017, C-022, C-023, C-024, C-033);
the remaining 26 were reviewed via the v2.0 portal. This blanket attestation covers
all 37 at their stated grades. Nothing was upgraded by this attestation.

**Effect:** claims move from DRAFT to ATTESTED. Merkle seal withheld pending the
issuer's explicit seal instruction.

## 2026-10-11 — Merkle seal implemented (corrected)

**Issuer instruction (verbatim):** "Let's implement the Merkle seal."

**Scheme:** SHA-256 binary Merkle tree. Leaves = sha256 of raw file bytes, ordered
by relative path lexicographically. Parent = sha256(hex(left) + hex(right)) with
lowercase hex digests concatenated as ASCII; an odd trailing node is duplicated.
**Leaves (42):** the 37 attested claim files (claims/C-001/claim.json … C-037) +
ATTESTATIONS.md + EXCLUSIONS.md + ROADMAP.md + LEDGER.md + README.md.
**Envelope (not leaves):** manifest.json (carries the root), seal.json (carries the
full tree), hashes.sha256 (derived file hashes).
**Sealed at:** 2026-10-12T01:16 UTC (2026-10-11 EDT), corrected 2026-10-12T01:25 UTC.
**Canonical root:** recorded in `ledger-package/seal.json` and `ledger-package/manifest.json`.
**Scope note:** the seal covers the ledger data. The HTML companion is a presentation
artifact and is NOT covered by this seal.
**Effect:** the v1 ledger is immutable as issued. Any future change to a claim,
grade, or register requires a new version, not an edit — corrections go forward.

*Correction note: an earlier root value (611f8ec7…) was computed before the
attestation record and manifest were finalized, so it did not match the shipped
files. It is superseded by the canonical root in seal.json.*

## 2026-10-12 — Ledger v2 issued (supersedes v1)

**Basis:** issuer instruction "Yes please" (2026-10-11) to fold independent review
R-2026-10-11-SOL's findings into a v2 cut and record the review as structured evidence.

**v2 changes:**
- C-008: statement amended (per-surface honesty; Slack removed from deployed set); grade verified→partial.
- C-017: rescoped to component assertions (A1 verified; A2–A3 partial; A4–A5 planned); grade verified→partial.
- C-013: statement clarified (implemented module vs spec-stage vision); grade unchanged (verified).
- Governing docs corrected: LEDGER.md (attested index, 23/12/2), README.md (v2 status + non-propagation invariant), ROADMAP.md (promotion view built; review-driven items).
- Language layering across all 37 claims: public narrative vs derivation_history vs assessment_notes.
- Evidence dimensions added: access / independence / reproducibility on every evidence item.
- Review record: reviews/R-2026-10-11-SOL.md (first structured review object).

**Grade distribution (v2):** 23 verified / 12 partial / 2 planned (37 claims).
**Note:** v1's seal remains valid for v1's files. v2 is a superseding release with its own seal, per corrections-go-forward.
