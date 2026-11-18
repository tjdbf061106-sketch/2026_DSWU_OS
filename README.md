# SynthEx–Solar Pro 4 aspirin run

This repository preserves a reproducible classroom record for an aspirin retrosynthesis request.

## Outcome

OpenCode resolved `upstage/solar-pro4` and completed a live model call. The model proposed one retrosynthetic transformation: salicylic acid + acetic anhydride → aspirin (phenolic O-acetylation). It did not provide conditions or yields; none are inferred here.

The installed native SynthEx source was also checked. Its supplied source tree contains no Solar/Upstage adapter, and its Windows offline demo stopped with a checkpoint-digest mismatch. That configuration/runtime failure is recorded separately from the completed OpenCode/Solar call.

## Contents

- `skills/synthex-report/`: reusable execution and evidence-reporting skill.
- `runs/aspirin-solar-opencode/`: raw OpenCode event log, invocation, extracted result, and summary.
- `reports/synthex_solar_aspirin_execution_report.pdf`: PDF report of installation, success, failure, and raw-record locations.

The proposal is AI-generated and is not an experimentally validated synthesis protocol.
