"""
Unified Documentation Pipeline Orchestrator
=============================================

Single-command entry point that runs the full documentation build pipeline:

1. Python lint check
2. Docstring coverage (interrogate — non-blocking)
3. Diagram generation (AST-based)
4. Sphinx build (primary docs)
5. MkDocs build (legacy docs)
6. Report generation (docs_report.json)
7. Optional: serve locally

Usage
-----
    # Full pipeline with local server
    python run_pipeline.py

    # Build only (no server)
    python run_pipeline.py --build-only

    # Skip coverage check (faster iteration)
    python run_pipeline.py --skip-coverage

    # Sphinx only (no MkDocs)
    python run_pipeline.py --sphinx-only
"""

import subprocess
import sys
import os
import json
import argparse
from datetime import datetime
from pathlib import Path


# ─── Constants ───────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent
SITE_DIR = PROJECT_ROOT / "site"
SPHINX_SRC = PROJECT_ROOT / "docs"
SPHINX_OUT = SITE_DIR / "sphinx"
MKDOCS_OUT = SITE_DIR / "legacy-docs"
REPORT_PATH = PROJECT_ROOT / "docs_report.json"


def get_python_exe() -> str:
    """
    Detect the correct Python executable, preferring a local venv.

    Returns
    -------
    str
        Path to the Python executable.
    """
    venv_python = PROJECT_ROOT / "venv" / "Scripts" / "python.exe"
    if venv_python.exists():
        print(f"📌 Using local venv: {venv_python}")
        return str(venv_python)

    # Try Unix-style venv
    venv_python_unix = PROJECT_ROOT / "venv" / "bin" / "python"
    if venv_python_unix.exists():
        print(f"📌 Using local venv: {venv_python_unix}")
        return str(venv_python_unix)

    print(f"⚠️  Venv not found. Using system Python: {sys.executable}")
    return sys.executable


def run_step(name: str, command: str, cwd: str = ".",
             non_blocking: bool = False) -> bool:
    """
    Execute a shell command as a pipeline step.

    Parameters
    ----------
    name : str
        Display name for the pipeline step.
    command : str
        Shell command to execute.
    cwd : str, optional
        Working directory for the command. Default is ``"."``.
    non_blocking : bool, optional
        If True, log warnings but don't fail the pipeline on error.
        Default is False.

    Returns
    -------
    bool
        True if the step succeeded (or was non-blocking), False if it failed.
    """
    print(f"\n{'═' * 60}")
    print(f"🚀 STEP: {name}")
    print(f"   Command: {command}")
    print(f"{'═' * 60}")

    result = subprocess.run(command, shell=True, cwd=cwd,
                            capture_output=True, text=True)

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        if non_blocking:
            print(f"⚠️  WARNING: {name} reported issues (non-blocking)")
            return True  # Don't fail the pipeline
        else:
            print(f"❌ FAILED: {name} exited with code {result.returncode}")
            return False

    print(f"✅ SUCCESS: {name}")
    return True


def run_interrogate(python_exe: str) -> dict:
    """
    Run interrogate docstring coverage check and parse results.

    Parameters
    ----------
    python_exe : str
        Path to the Python executable.

    Returns
    -------
    dict
        Coverage report with ``coverage_pct``, ``total``, ``covered``, ``missing``.
    """
    print(f"\n{'═' * 60}")
    print("🔍 STEP: Docstring Coverage Check (interrogate)")
    print(f"{'═' * 60}")

    result = subprocess.run(
        f"{python_exe} -m interrogate backend/ -v --fail-under 0",
        shell=True,
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr
    print(output)

    # Parse coverage from output
    coverage_data = {
        "coverage_pct": 0.0,
        "total": 0,
        "covered": 0,
        "missing": 0,
        "status": "unknown"
    }

    for line in output.splitlines():
        if "RESULT" in line.upper() or "%" in line:
            # Try to extract percentage
            import re
            match = re.search(r'(\d+\.?\d*)%', line)
            if match:
                coverage_data["coverage_pct"] = float(match.group(1))

    if float(coverage_data["coverage_pct"]) >= 90:
        coverage_data["status"] = "excellent"
        print("✅ Docstring coverage is excellent!")
    elif float(coverage_data["coverage_pct"]) >= 70:
        coverage_data["status"] = "good"
        print("⚠️  Docstring coverage is acceptable but could improve.")
    else:
        coverage_data["status"] = "needs_improvement"
        print("⚠️  Docstring coverage needs improvement.")

    print("ℹ️  Note: This check is non-blocking (will not fail the build)")
    return coverage_data


def generate_report(
    sphinx_success: bool,
    mkdocs_success: bool,
    coverage_data: dict,
    diagrams_report: dict
) -> dict:
    """
    Generate the docs_report.json feedback artifact.

    Parameters
    ----------
    sphinx_success : bool
        Whether the Sphinx build succeeded.
    mkdocs_success : bool
        Whether the MkDocs build succeeded.
    coverage_data : dict
        Interrogate coverage results.
    diagrams_report : dict
        Diagram generation report.

    Returns
    -------
    dict
        Complete documentation report.
    """
    report = {
        "timestamp": datetime.now().isoformat(),
        "pipeline_version": "1.0.0",
        "builds": {
            "sphinx": {
                "success": sphinx_success,
                "output_dir": str(SPHINX_OUT),
            },
            "mkdocs": {
                "success": mkdocs_success,
                "output_dir": str(MKDOCS_OUT),
            },
        },
        "coverage": coverage_data,
        "diagrams": diagrams_report,
        "warnings": [],
    }

    warnings_list = []
    if not sphinx_success:
        warnings_list.append("Sphinx build failed")
    if not mkdocs_success:
        warnings_list.append("MkDocs build failed")
    if coverage_data.get("status") == "needs_improvement":
        warnings_list.append(
            f"Docstring coverage is {coverage_data.get('coverage_pct', 0)}%"
        )
    report["warnings"] = warnings_list

    # Write report
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"\n📄 Report saved to {REPORT_PATH}")
    return report


def main():
    """
    Main pipeline entry point.

    Parses command-line arguments and executes all pipeline steps
    in sequence, generating a final docs_report.json artifact.
    """
    parser = argparse.ArgumentParser(
        description="AutoCodeDoc Unified Documentation Pipeline"
    )
    parser.add_argument(
        "--build-only", action="store_true",
        help="Run all checks and builds without starting a server"
    )
    parser.add_argument(
        "--skip-coverage", action="store_true",
        help="Skip the interrogate docstring coverage check"
    )
    parser.add_argument(
        "--sphinx-only", action="store_true",
        help="Build only Sphinx docs (skip MkDocs)"
    )
    parser.add_argument(
        "--serve", action="store_true", default=True,
        help="Start local Sphinx dev server after build (default)"
    )
    args = parser.parse_args()

    if args.build_only:
        args.serve = False

    python_exe = get_python_exe()

    print("\n" + "═" * 60)
    print("   AutoCodeDoc Documentation Pipeline v1.0")
    print("═" * 60)

    # ── Step 1: Lint Check ──────────────────────────────────────────────
    if not run_step(
        "Python Lint Check",
        f"{python_exe} -m py_compile backend/app/main.py",
        cwd=str(PROJECT_ROOT)
    ):
        print("ℹ️  Lint check failed — continuing anyway for docs build")

    # ── Step 2: Docstring Coverage (non-blocking) ───────────────────────
    coverage_data = {"status": "skipped", "coverage_pct": 0}
    if not args.skip_coverage:
        coverage_data = run_interrogate(python_exe)
    else:
        print("\n⏭️  Skipping coverage check (--skip-coverage)")

    # ── Step 3: Diagram Generation ──────────────────────────────────────
    diagrams_report = {}
    if not run_step(
        "Diagram Generation",
        f"{python_exe} scripts/generate_diagrams.py",
        cwd=str(PROJECT_ROOT)
    ):
        print("⚠️  Diagram generation had issues — continuing build")
        diagrams_report = {"error": "generation failed"}
    else:
        # Load diagrams report if available
        diagrams_json = PROJECT_ROOT / "diagrams_report.json"
        if diagrams_json.exists():
            with open(diagrams_json, "r") as f:
                diagrams_report = json.load(f)

    # ── Step 4: Sphinx Build (Primary) ──────────────────────────────────
    os.makedirs(SPHINX_OUT, exist_ok=True)
    sphinx_success = run_step(
        "Sphinx Build (Primary Docs)",
        f"{python_exe} -m sphinx -b html -W \"{SPHINX_SRC}\" \"{SPHINX_OUT}\"",
        cwd=str(PROJECT_ROOT)
    )

    # ── Step 5: MkDocs Build (Legacy) ───────────────────────────────────
    mkdocs_success = True
    if not args.sphinx_only:
        os.makedirs(MKDOCS_OUT, exist_ok=True)
        mkdocs_success = run_step(
            "MkDocs Build (Legacy Docs)",
            f"{python_exe} -m mkdocs build -d \"{MKDOCS_OUT}\"",
            cwd=str(PROJECT_ROOT)
        )
    else:
        print("\n⏭️  Skipping MkDocs build (--sphinx-only)")

    # ── Step 6: Generate Report ─────────────────────────────────────────
    report = generate_report(sphinx_success, mkdocs_success,
                             coverage_data, diagrams_report)

    # ── Summary ─────────────────────────────────────────────────────────
    print(f"\n{'═' * 60}")
    print("   PIPELINE COMPLETE")
    print(f"{'═' * 60}")
    print(f"   Sphinx Build:  {'✅' if sphinx_success else '❌'}")
    print(f"   MkDocs Build:  {'✅' if mkdocs_success else '❌' if not args.sphinx_only else '⏭️ skipped'}")
    print(f"   Coverage:      {coverage_data.get('coverage_pct', 'N/A')}%")
    print(f"   Diagrams:      {diagrams_report.get('diagrams_generated', 'N/A')} generated")
    print(f"   Report:        {REPORT_PATH}")
    print(f"{'═' * 60}")

    if not sphinx_success:
        sys.exit(1)

    # ── Step 7: Optional Serve ──────────────────────────────────────────
    if args.serve:
        print(f"\n🌐 Starting Sphinx dev server at http://127.0.0.1:8002")
        print("   Press Ctrl+C to stop.\n")
        run_step(
            "Sphinx Dev Server",
            f"{python_exe} -m http.server 8002 --directory \"{SPHINX_OUT}\"",
            cwd=str(PROJECT_ROOT)
        )


if __name__ == "__main__":
    main()
