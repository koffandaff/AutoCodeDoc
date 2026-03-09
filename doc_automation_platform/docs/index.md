# Developer Platform Overview

Welcome to the Documentation Automation MVP!

This site demonstrates the power of **Docs as Code**. It automatically extracts docstrings directly from the Python (FastAPI) backend and serves them here dynamically.

## Features Included

- FastAPI Backend with Google-style docstrings
- Next.js Client application (Frontend)
- Custom AST Parser for Architecture Diagram generation
- MkDocs configuration using `material` theme
- API block injections utilizing `mkdocstrings`

## 🚀 Quick Navigation

*   **[API Reference](app/)** - This is where your code is documented!
*   **[Architecture Overview](architecture.md)** - See how modules connect.
*   **[Installation Guide](installation.md)** - Get up and running.
*   **[Tutorials](tutorials/weather_model_training.ipynb)** - Learn with notebooks.
*   **[Navigation Test](test.md)** - Verify the system!

## Working Locally

To see the live docs when changing code:

```bash
python scripts/run_pipeline.py
```

The site will be available at: **[http://127.0.0.1:8001/AutoCodeDoc/](http://127.0.0.1:8001/AutoCodeDoc/)**
