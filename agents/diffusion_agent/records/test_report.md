# Test and revision report

Date: November 1, 2026. Runtime: the current interactive Codex conversation; local Python for validation. See run_provenance.md for the distinction between model-authored outputs and local checks.

## Primary and context contrast

| Case | Held constant | Changed | Result |
|---|---|---|---|
| Primary | Generative AI and dated evidence | Fast-follower B2B support drafting with human review | Timely six-week reversible learning, subject to accountable approval |
| Contrast 1 | Same technology, application, organization, evidence and capabilities | Conservative posture and corresponding management question only | Same general and application findings; offline evidence first, customer exposure later |
| Contrast 2 | Same technology and evidence | Automatic credit-denial explanations, retail bank, sensitive data, high consequences, aggressive posture | Same general finding; application stage unknown; offline or shadow evaluation before any release proposal |

## Actual preserved weakness and revision

The initial model-authored v0.1 draft added a top-level rogers_assessment. The frozen output schema sets additionalProperties to false, so this draft violated the interface even though the provided lightweight validator printed VALIDATION PASSED. The specialist checker reports: $: forbidden extra field rogers_assessment. The initial response, metadata and less-explicit placement instructions are retained in history/v0.1. This was an observed local contract failure, not a fabricated business incident.

Version 0.2 explicitly places the five-factor reasoning in application_finding and organizational interpretation in organization_specific_finding, retaining the fixed schema. The regression checker detects the old error and accepts all three corrected responses. Neither the frozen schema nor its validator was changed. Its extra-field blind spot remains documented.

## Recorded checks and substantive review

All 15 automated checks in check_results.json pass. The course validator accepts the three final responses and the frozen integrity checker reports FROZEN CORE INTACT. Automated checks cover required types, forbidden top-level fields, the intended case differences, shared technology/evidence, general-finding stability, contextual variation and seven frozen hashes. They do not verify claims or prove independent model behavior.

The assistant additionally reviewed each saved output against the assignment: five Rogers characteristics and adopter categories are addressed; application and industry uncertainty are explicit; roles and mechanisms are qualified as proposed or inferred; timing changes have stated reasons; high consequence dominates an aggressive posture; majority peer penetration is not asserted; the full adoption decision is handed off. This is an in-session qualitative review, not a blinded human evaluation or accuracy score.

## Remaining weakness and next test

No representative application-specific peer diffusion data was available in the bounded source packet. The application stage and peer rank therefore remain unknown. Exact equality of the saved general findings was deliberately preserved by reusing a shared evidence conclusion; it is a consistency control, not proof that a fresh unassisted model run will remain stable. A useful next test is a fresh-session posture swap with an independent reviewer and updated same-unit peer evidence. No such test is claimed here.
