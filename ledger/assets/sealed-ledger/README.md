# Capability Ledger — Keith Soyka (live personal ledger)

This is the REAL ledger: Keith's own capability record, sourced from the
accomplishments spreadsheet and held to evidence-grade rigor.

- Source: `workspace/user/files/Keith_Soyka_Accomplishments_and_Capabilities_3_wwv7.xlsx`
  (434 rows, mergence of AI assessments — treated as UNVERIFIED input, never as findings)
- Rule: no AI output is ever a finding. Every claim carries an evidence grade
  (verified / partial / planned / unsupported). v1 shipped DRAFT; the issuer
  attested all 37 claims 2026-10-11 ("I attest the claims and their strict
  boundary controls"); v2 amends per independent review R-2026-10-11-SOL.
- This is NOT the v1 prototype at `workspace/capability-ledger-prototype/`.
  That is a frozen function demo using Keith as the sample case. Do not merge
  the two. Do not bolt new claims onto the prototype.

## Layout
- `_analysis/` — working analysis (manifest, notes). Not part of any sealed package.
- `claims/<id>/` — one directory per attested-track claim: `claim.json` + `evidence/`.
- Claim file schema mirrors the prototype: id, statement, category,
  date_range, evidence_grade, how_and_why, evidence[] (artifact_id,
  descriptor, function, disclosure, provenance, captured_at, package_path,
  sha256, bytes), plus `status` (DRAFT until attested; no leaf_hash until sealed).

## Pipeline
spreadsheet rows → dedupe/cluster → grade → draft claims → Keith attests →
seal (hash + merkle root) → publish package.

## Design principles (issuer, 2026-10-11)

1. **The journey is the knowledge.** A ledger that packages only clean outputs
   teaches nothing and risks repeating failures. Claims carry their red-to-green
   history: the failure, the fix, the implementation — not just the final state.
2. **Red-to-green is evidence.** A 732/734 run with named failures followed by a
   734/734 run is stronger evidence than a lone green run, because it shows the
   failure was understood and fixed, not hidden.
3. **No AI output is ever a finding.** Every claim ships DRAFT until the issuer
   verdicts it: attest / edit / re-grade / drop.
4. **Gaps are labeled, not filled.** Unverifiable figures are excluded or gated,
   never smoothed over. See EXCLUSIONS.md.
5. **Corrections go forward.** Originals are preserved and amended in the corpus;
   the ledger records what changed and why.
6. **Attestation does not propagate.** No conclusion may inherit the attestation
   status of its supporting artifacts. An artifact may be authentic while
   irrelevant; relevant while insufficient. Every transition from artifact to
   conclusion requires its own attributed assessment and issuer disposition.
   (Adopted from independent review R-2026-10-11-SOL; consistent with the
   ledger's standing "no AI output is ever a finding" rule.)
7. **Grade by the weakest material assertion.** A claim's overall grade defaults
   to its least-supported material assertion unless the statement excludes it.
   Compound claims carry per-assertion grades.
