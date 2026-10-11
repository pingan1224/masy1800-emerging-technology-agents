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
