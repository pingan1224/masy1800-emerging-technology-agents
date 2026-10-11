# Banking Disruption Specialist

Coursework analysis of a hypothetical employee-assisted AI agent for credit-card billing disputes. This specialist evaluates creative destruction and management response; it does not access accounts or handle real complaints.

The tested instructions are version 0.3. Three case JSON files and complete generated prompts are provided. records/actual_runs contains four real ChatGPT outputs and screenshots; records/test_comparison.md and observed_weakness_and_revision.md explain the observed baseline weakness and independent retest. responses/ contains earlier Codex-authored candidates and a clearly labeled diagnostic fixture, which are historical development material and do not count as actual trials.

The common instructions, schemas and course tools are unchanged. Validate captured responses with tools/validate_response.py and check frozen files with tools/check_frozen_core.py. All constraints present in the frozen output schema were also checked recursively. This additional check supports only the schema's actual keywords, not the entire JSON Schema standard. Passing these checks does not establish financial outcomes or model reliability.

See records/agent_record.md and github_version_record.json for provenance and version history. Sources and all bank/provider cases have explicit evidence boundaries. The student's independent judgment and reflection require personal review.
