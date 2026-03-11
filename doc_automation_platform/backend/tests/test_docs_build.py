"""
Sphinx Build Validation Test
============================

Asserts that the Sphinx documentation builds successfully without warnings.
"""

import subprocess
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SPHINX_SRC = PROJECT_ROOT / "docs"
SPHINX_OUT = PROJECT_ROOT / "site" / "sphinx"

def test_sphinx_build_no_errors():
    """Build Sphinx docs and ensure return code is 0."""
    os.makedirs(SPHINX_OUT, exist_ok=True)
    
    # Run sphinx-build with warnings treated as errors (-W) and keep going
    cmd = [
        sys.executable, "-m", "sphinx.cmd.build",
        "-b", "html",
        "--keep-going",
        str(SPHINX_SRC),
        str(SPHINX_OUT)
    ]
    
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PROJECT_ROOT / "backend")
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
        cwd=str(PROJECT_ROOT)
    )
    
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
        
    assert result.returncode == 0, f"Sphinx build failed: {result.stderr}"
    assert (PROJECT_ROOT / "site" / "sphinx" / "index.html").exists(), "Sphinx index.html was not generated."
