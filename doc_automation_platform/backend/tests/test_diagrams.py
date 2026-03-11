"""
Diagram Generation Validation Test
==================================

Assures that diagram generation scripts output valid files with content.
"""

import os
import subprocess
import sys
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ARCH_DIR = PROJECT_ROOT / "docs" / "architecture"
REPORT_PATH = PROJECT_ROOT / "diagrams_report.json"

def test_diagram_files_exist_and_populated():
    """Run diagram generator and check output files."""
    # First, run the generation script
    cmd = [sys.executable, "scripts/generate_diagrams.py"]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PROJECT_ROOT / "backend")
    env["PYTHONIOENCODING"] = "utf-8"
    
    subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
        env=env,
        check=True
    )
    
    # Verify the architecture markdown files
    expected_files = [
        "system_diagram.md",
        "er_diagram.md",
        "cross_repo_flow.md"
    ]
    
    for filename in expected_files:
        filepath = ARCH_DIR / filename
        assert filepath.exists(), f"Expected diagram file missing: {filepath}"
        assert filepath.stat().st_size > 100, f"Diagram file {filepath} seems empty or too small"
        
        # Check for mermaid tags indicating successful embedding
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            assert "```{mermaid}" in content, f"Mermaid tag missing in {filename}"
            if filename == "er_diagram.md":
                assert "erDiagram" in content, f"erDiagram keyword missing in {filename}"
            elif filename == "system_diagram.md":
                assert "graph TD" in content, f"graph TD keyword missing in {filename}"

def test_diagram_report_generated():
    """Verify that the diagrams_report.json is correctly generated."""
    assert REPORT_PATH.exists(), f"Report file missing: {REPORT_PATH}"
    
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    assert "diagrams_generated" in data
    assert data["diagrams_generated"] == 3
    assert "system_architecture" in data
    assert "er_diagram" in data
