---
name: synthex-report
description: Run a supplied SynthEx workflow for a molecule and create an evidence-linked success or failure report. Use when the installed adapter, model configuration, and command are available; do not silently substitute providers.
---

# SynthEx execution and report

## Inputs

Collect the molecule name, valid SMILES, the supplied SynthEx command/configuration, and a new output directory. Keep API credentials only in environment or client credential storage; never include them in prompts, commands, manifests, logs, or reports.

## Run

1. Preflight the source revision, configured adapter/model, command, and write location. Do not modify the SynthEx source or swap providers when the configured adapter is absent.
2. Run within the supplied budget and preserve the original output. Do not overwrite a completed run.
3. Save `manifest.json`, original model responses, stdout/stderr, and any validation output. If no native adapter is available but the user explicitly requests a harness run, record it as a separate harness result rather than calling it a native SynthEx run.

## Report

Report only artifact-backed facts: source revision, model ID, target, status, stage, route content, and errors. Separate configuration/connection failures from route-planning failures. If planning fails, record the stopping stage and error; do not invent a route, conditions, yields, or validation result.

For a proposed route, state clearly that it is not experimentally validated.
