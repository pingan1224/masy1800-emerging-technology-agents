# Emerging Technology Diffusion Agent

Version 0.2.0, November 1, 2026. Interactive ChatGPT/Codex specialist created from the supplied course template. No API or model account is required. Local code builds prompts and validates saved responses; it does not generate an analysis.

From the scaffold root, run with Python 3:
```
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/primary.json
```
Submit the entire resulting work/diffusion_agent_primary_prompt.txt to ChatGPT, save its JSON response, then run:
```
python tools/validate_response.py agents/diffusion_agent/responses/primary_response.json
python agents/diffusion_agent/check_specialist.py
```
Repeat the build for contrast_1 and contrast_2. The optional specialist checker uses the standard library, enforces the full frozen contract and checks a few explicit regression properties. It does not assess truth or independently establish general model reliability. Inspect evidence/source_register.md and records/test_report.md before team integration. All cases are hypothetical and saved responses are model-authored in this Codex conversation.
