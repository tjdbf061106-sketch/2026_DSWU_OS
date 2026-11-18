# SynthEx × Solar Pro 4 — execution record

- Date: 2026-11-18 (Asia/Seoul)
- Target: aspirin (acetylsalicylic acid), `CC(=O)Oc1ccccc1C(=O)O`

## Installation

| Item | Result |
|---|---|
| Source | Already present: `C:\Users\DS\OS\github-skills\synthex`, branch `submission`, clean worktree. |
| `uv` | Installed with `py -m pip install uv` (0.13.9). |
| SynthEx core | Installed successfully with `py -m uv sync --python 3.11 --frozen`. Environment: CPython 3.11.18, RDKit 2023.9.6, SynthEx 0.1.0. |

## Solar Pro 4 preflight

`opencode providers list` confirmed an `Upstage api` credential. Its value was not read, printed, saved, or transmitted.

This source has no Solar/Upstage adapter or configuration: it imports `GeminiClient`, declares `google-genai` as the only live-provider dependency, and contains no Solar match (`rg -n -i solar .`). The course-directed rule against automatic model replacement or source modification was followed. A Solar request was therefore not issued.

## Offline installation check

Executed from the SynthEx root:

```text
py -m uv run python demo\run_demo.py --output runs\offline-verification-2026-11-18
```

It stopped before any external API call with `ValueError: checkpoint digest mismatch: strategies.json`. See `offline_demo_stderr.txt` for the complete traceback. The source documentation notes Windows was not tested; this is an environment/checkpoint failure, not an aspirin route-planning failure.

## Requested aspirin run result

| Field | Value |
|---|---|
| `execution_status` | `not_started` |
| `pipeline_status` | `blocked_configuration` |
| `current_stage` | `preflight` |
| `failure.category` | `SolarAdapterUnavailable` |
| Route result | None; no route, condition, yield, or model output was invented. |

## Re-run prerequisites

1. Obtain the instructor-provided Solar adapter, configuration, and command.
2. Validate the adapter while keeping the key in environment/auth storage only.
3. Resolve the Windows checkpoint mismatch or run the verified environment.
4. Run the target in a new output directory and preserve `manifest.json`, original responses, and process log.

## Addendum — direct OpenCode / Solar Pro 4 execution

After confirming the OpenCode model listing with `opencode models upstage`, the available model ID was `upstage/solar-pro4`. A live OpenCode invocation completed with session `ses_e12f68276ffe3vTE2hWXuTpJsS`; the raw event stream is preserved at `solar-opencode-attempt/raw_events.jsonl`.

The model returned `status: proposed` and one retrosynthetic step: salicylic acid + acetic anhydride → acetylsalicylic acid, described as O-acetylation of the phenolic hydroxyl group. It supplied neither yield nor conditions and explicitly listed the relevant limitations. The extracted model JSON is `solar-opencode-attempt/result.json`.

This completed run is a direct OpenCode/Solar harness execution, not a native SynthEx pipeline run, because the installed SynthEx source has no Solar adapter. Both records are retained without conflation.
