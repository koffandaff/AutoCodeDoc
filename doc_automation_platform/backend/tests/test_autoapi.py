"""
AutoAPI Validation Test
=======================

Checks that sphinx-autoapi successfully generates API index files
and documents key modules (endpoints, schemas, services, utilities).
"""

import os
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
# AutoAPI outputs `.rst` files to `docs/sphinx/api` during build
API_OUT_DIR = PROJECT_ROOT / "docs" / "api"

def test_autoapi_index_exists():
    """Verify that autoapi generated the root index.rst."""
    index_path = API_OUT_DIR / "index.rst"
    assert index_path.exists(), f"AutoAPI index not generated at {index_path}"
    
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "API Reference" in content
        assert "app" in content

def test_key_modules_documented():
    """Check that essential modules are present in the generated API docs."""
    # We expect `app.api.users`, `app.models.user`, `app.services.user_service` 
    # and `app.utils.validation` to be documented.
    
    expected_files = [
        "app/api/users/index.rst",
        "app/models/user/index.rst",
        "app/services/user_service/index.rst",
        "app/utils/validation/index.rst"
    ]
    
    for filename in expected_files:
        filepath = API_OUT_DIR / filename
        assert filepath.exists(), f"AutoAPI missing expected module: {filepath}"
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            # Verify its a python module doc
            assert ".. py:module::" in content or "Module Contents" in content
