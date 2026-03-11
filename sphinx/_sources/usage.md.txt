# Usage Guide

This project automatically generates API documentation by reading the docstrings inside your FastAPI components (`backend/app/api`, `backend/app/services`, and `backend/app/models`).

### Adding a new API Endpoint

When you create a new Python module, `doc_automation_platform` dynamically renders it!
For example:

1. Create `backend/app/api/new_feature.py`.
2. Add a basic FastAPI router, and provide a single Google-style Docstring string under your function definition.
3. Once saved, `mkdocs-gen-files` will pick it up automatically during `mkdocs serve` or `mkdocs build`.

The system also auto-links nested models to their appropriate service schemas.
