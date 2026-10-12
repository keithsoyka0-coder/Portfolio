# Ledger Attestations

Issuer: Keith Soyka. No AI output is ever a finding; an attestation below is the
issuer's own verdict, recorded verbatim.

## 2026-10-11 — Capability Ledger Prototype v2.0 (artifact attestation)

**Issuer statement (verbatim):** "I attest the v2 prototype"

**Scope of this attestation:** the v2.0 portal ARTIFACT itself — i.e., it faithfully
presents the ledger package contents (37 draft claims, grade distribution 25/10/2,
exclusions register, design principles, red-to-green journey records) as they stand.

**Explicitly NOT covered:** per-claim attestation. At that point, the 37 claims remained DRAFT pending
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
