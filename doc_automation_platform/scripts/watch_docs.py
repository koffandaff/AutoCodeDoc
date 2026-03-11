"""
Auto-Reloading Development Server
=================================

This script watches the source code and documentation files for changes
and automatically rebuilds the Sphinx documentation and refreshes your browser.

Usage:
    python scripts/watch_docs.py
"""

import os
import sys
import subprocess
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
OUTPUT_DIR = PROJECT_ROOT / "site" / "sphinx"
BACKEND_DIR = PROJECT_ROOT / "backend"

def run_watcher():
    """Start the sphinx-autobuild server."""
    print("🚀 Starting Live Documentation Server...")
    print(f"📁 Watching: {DOCS_DIR}")
    print(f"📁 Watching: {BACKEND_DIR}")
    print(f"🌐 Server will be at: http://127.0.0.1:8000")
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Command for sphinx-autobuild
    # -b html: Build HTML
    # --watch: Also watch the backend/app directory for code/docstring changes
    # --open-browser: Open the browser automatically
    cmd = [
        sys.executable, "-m", "sphinx_autobuild",
        str(DOCS_DIR),
        str(OUTPUT_DIR),
        "--watch", str(BACKEND_DIR / "app"),
        "--ignore", "**/__pycache__/*",
        "--ignore", "**/api/*",  # Avoid loop if autoapi emits files to build dir
        "--port", "8000",
        "--open-browser"
    ]
    
    # Set PYTHONPATH so autoapi can import the backend
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BACKEND_DIR)
    
    try:
        subprocess.run(cmd, env=env, check=True)
    except KeyboardInterrupt:
        print("\n👋 Stopping server...")

if __name__ == "__main__":
    run_watcher()
