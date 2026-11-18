"""Create a new evidence-preserving run directory for the final project."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Path to the target input JSON")
    parser.add_argument("--run-id", required=True, help="New, unique run identifier")
    parser.add_argument("--output-root", default="runs")
    args = parser.parse_args()

    target_path = Path(args.target)
    target = json.loads(target_path.read_text(encoding="utf-8"))
    missing = [key for key in ("target_id", "name", "smiles", "selection_rationale") if not target.get(key)]
    if missing:
        raise SystemExit(f"Target input is missing required fields: {', '.join(missing)}")

    run_dir = Path(args.output_root) / args.run_id
    if run_dir.exists():
        raise SystemExit(f"Run directory already exists and will not be overwritten: {run_dir}")

    for name in ("route", "conditions", "yield", "structures", "report"):
        (run_dir / name).mkdir(parents=True, exist_ok=False)
    (run_dir / "input.json").write_text(json.dumps(target, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "run_id": args.run_id,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "prepared",
        "target_input": "input.json",
        "model_configuration": "config/project.local.yaml",
        "artifacts": {"route": [], "conditions": [], "yield": [], "structures": [], "report": []},
        "failures": [],
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(run_dir)


if __name__ == "__main__":
    main()
