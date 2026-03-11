"""
Docstring Coverage Validation Test
===================================

Runs interrogate and asserts that a coverage report is produced.
Since the mentor specified non-blocking, we don't assert over a specific percentage
here, but we verify the tool runs successfully.
"""

import subprocess
import os
import sys
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

def test_interrogate_coverage_runs():
    """Run interrogate and verify it outputs a valid coverage percentage."""
    cmd = [
        sys.executable,
        "-m", "interrogate",
        "backend/",
        "-v",
        "--fail-under", "0"
    ]
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT)
    )
    
    assert result.returncode == 0, f"Interrogate failed: {result.stderr}"
    
    # Check that it output a RESULT line with a percentage
    output = result.stdout + result.stderr
    assert "RESULT:" in output, "Expected 'RESULT:' in interrogate output"
    
    # Extract percentage to ensure it parsed correctly
    match = re.search(r'RESULT:.* (\d+\.\d+)%', output)
    assert match is not None, "Could not extract coverage percentage."
    pct = float(match.group(1))
    assert 0.0 <= pct <= 100.0, "Coverage percentage out of bounds."
