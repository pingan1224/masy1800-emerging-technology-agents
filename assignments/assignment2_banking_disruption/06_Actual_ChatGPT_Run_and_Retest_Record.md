# Observed weak output, revision and actual retest

All four trials were executed in fresh ChatGPT conversations on 11 October 2026. Complete generated prompt packets were pasted as text attachments, with an execution instruction. Trials used the supplied source register and did not browse. The visible model label was ChatGPT, with Medium thinking strength; the exact underlying model identifier was not exposed. Completion was observed before capture. Raw responses, exact prompt files, conversation URLs and run metadata are preserved.

## Baseline observation: run 01, v0.1
The actual baseline was cautious about evidence and recommended a bounded employee-assisted evaluation. It did not claim that banks were certainly being displaced. Its weaknesses were specificity and scope:

1. In organization_specific_finding it used "low-to-moderate" for the bank and "moderate-to-high" for an additional hypothetical outsourcing provider, rather than a single required potency category.
2. It assigned a "near-term operational evaluation horizon" while conceding that material organizational impact in that period was unestablished. This conflates pilot scheduling with the matrix's material-impact horizon.
3. It did not identify one exact Figure 1.8 cell and its default management action. It mixed a contrast organization into the primary response without a complete contrast case.

The initial prompt helped cause these weaknesses: it requested an outsider comparison without that organization's full case and lacked explicit single-label and material-horizon requirements. A passed schema check therefore did not make the output satisfactory.

## Revision after observation: v0.3
The v0.2 instructions were earlier development work and are preserved as such. Following the actual baseline, v0.3 added a one-case boundary; exactly one potency, severity and material-impact horizon; an exact matrix cell/default action; explicit separation of pilot duration from material impact; and labeled baseline, creation, destruction, mechanism, incumbent dilemma and monitoring trigger. Common instructions, schemas and frozen tools were unchanged. The final instruction snapshot is records/specialist_instructions_v0.3.md.

## Independent primary retest: run 02
The response states "Potency: Moderate" and "Moderate severity / near-term material-impact horizon" with "pilot or partner." It describes near-term impact as a provisional, low-confidence planning assumption requiring operating evidence. It explicitly states that a 90-day evaluation does not prove material workflow change within 90 days. It keeps the economic exposure at the complaint-handling workflow and treats bank-wide existential disruption as unsupported. Thus the specific categorization, scope and timing weaknesses improved in this observed retest.

## Context contrasts: runs 03 and 04
The labor-hour-priced supplier receives High potency, High/mid-term, and "prepare and pilot," because reduced purchased hours could erode its main pricing logic. The bank lacking approved access and audit-ready integration receives Moderate potency, Moderate/mid-term, and "monitor and build optionality." Its response says that missing local readiness does not weaken the general technology capability.

Stable substantive finding: plausible assistance with information gathering and drafting; no demonstrated net savings, production readiness or autonomous resolution. Changed finding: the exposed economic unit, revenue mechanism, material-impact horizon and management action. The wording is not identical across actual runs, so stability is a reviewed substantive comparison, not an exact-string result.

## Remaining weaknesses and limits
Responses remain substantially longer than the specialist's 900-1,400-word target. Run 03 also contains visible punctuation/encoding artifacts (for example, replacement characters around separators and a malformed 12-36-month dash). The raw captured text is preserved rather than silently corrected. These issues merit a later concision/formatting revision; they do not reverse the observed single-label and material-horizon improvement.

This is one baseline, one primary retest and two context contrasts, not a statistical reliability study. Near/mid planning bins are scenario assumptions, not established forecasts. Proposed numerical gates in the actual outputs, including run 02's 10% effort target, are analyst proposals requiring management approval, not measured results or benchmarks. No actual bank outcomes, customer data, production integration or compliance determination were obtained. The earlier intentionally weak authored fixture remains in responses/ as a labeled historical development example and is not counted as an observed run.

# Actual ChatGPT test comparison

| Run | Instructions / context | Observed classification | Matrix action | Review |
| --- | --- | --- | --- | --- |
| 01 | v0.1 / primary bank | Low-to-moderate bank; moderate-to-high unspecified supplier | No single exact cell | Valid schema; weak specificity, mixed scope and evaluation/impact horizon |
| 02 | v0.3 / same primary bank | Moderate; Moderate / near-term | Pilot or partner | Specific labels; material horizon qualified; 90-day learning separated |
| 03 | v0.3 / labor-hour-priced provider | High; High / mid-term | Prepare and pilot | Main revenue exposure explains stronger potency; timing remains conditional |
| 04 | v0.3 / readiness-constrained bank | Moderate; Moderate / mid-term | Monitor and build optionality | Local readiness changes timing without downgrading general technology |

All four captured responses passed the course validator and the full frozen JSON schema. Review was performed by Codex against the course framework and supplied source register; it is not independent human adjudication. Single runs cannot establish reproducibility or predictive accuracy. The revised outputs exceed the requested word target, and run 03 has punctuation artifacts. No success claim is made about real banking operations.

## Conversation provenance

- 01_primary_v0: https://chatgpt.com/c/6acbf3db-45dc-83e8-a63d-716efbf9fdcf | 2957 response-value words | raw SHA-256 38058c4b2ef953d1a0cc63c78570dc5323bdde82b2f75af543af6178d785cc90

- 02_primary_v0_3: https://chatgpt.com/c/6acbf4b3-6178-83e9-b356-bbed8be09626 | 2692 response-value words | raw SHA-256 1ec0dabd1f172ce5f1c81d691b891cc6a2bdcfaf008ae6abe2170e7437382272

- 03_contrast_1_v0_3: https://chatgpt.com/c/6acbf504-996c-83ea-a304-e3810986aebf | 2544 response-value words | raw SHA-256 26b7e25d46512145d0b956895f1f663ebf6a41887248f262d9e465aa8c31ddc2

- 04_contrast_2_v0_3: https://chatgpt.com/c/6acbf5a5-3390-83e9-86e1-6d95d975727c | 2073 response-value words | raw SHA-256 fb26e71c88a263bc4f3db2cd2fb8ff6b8e6718d0ce2b7c4e26cc59a66c701f3d
