# Capability Ledger — attested claim index (v2)

37 claims, attested by the issuer 2026-10-11. This index supersedes the v1 draft
index (which recorded pre-attestation state and is preserved in the sealed v1 package).

## Grade distribution (v2)
- verified: 23
- partial: 12
- planned: 2

v2 changes: C-008 verified→partial (Slack overclaim corrected; per-surface states),
C-017 verified→partial (compound claim split into component assertions).

## By category
- Governance & Security: 8
- Business & Commercialization: 7
- Multi-Agent Orchestration: 6
- Developer Tooling: 6
- Data Layer & Retrieval: 4
- Creative Direction & Brand: 2
- Conversational Systems & Adapters: 1
- Voice & Multimodal: 1
- Evaluation & Observability: 1
- Operations Leadership: 1

## Grading rule (v2)
Overall grade defaults to the **least-supported material assertion** within the
claim, unless the statement is rewritten to exclude that assertion. Compound
claims carry a component `assertions` array with per-assertion grades.

## Attestation record
See ATTESTATIONS.md: prototype attestation, blanket claims attestation
("I attest the claims and their strict boundary controls," 2026-10-11),
Merkle seal record, and independent review R-2026-10-11-SOL.
