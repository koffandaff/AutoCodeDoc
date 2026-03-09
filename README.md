# AutoCodeDoc Platform 

A production-grade, automated documentation engine that turns your Python code into a beautiful, live-updating documentation site.

## Features

- **Automated API Reference**: Every FastAPI route is documented instantly with technical parameters, response types, and raises.
- **Dynamic Architecture Diagrams**: A custom AST (Abstract Syntax Tree) parser scans your Python imports to generate a real-time graph of how your API, Services, and Models connect.
- **Dynamic ER Diagrams**: True Entity-Relationship diagrams generated directly from your Pydantic models, including field-level attributes (Int, Str, etc.).
- **Doc Integrity Checker**: A recursive guardrail (`check_doc_sync.py`) that ensures all Pydantic fields have descriptions before allowing a build.
- **Single-Command Pipeline**: Run `python scripts/run_pipeline.py` to check integrity, generate diagrams, and serve/build the site in one go.

## Tech Stack

- **Core**: Python 3.x, FastAPI, Pydantic v2
- **Documentation**: [MkDocs](https://www.mkdocs.org/) with [Material Theme](https://squidfunk.github.io/mkdocs-material/)
- **Automation**: `mkdocstrings`, `mkdocs-gen-files`, `mkdocs-literate-nav`, `mkdocs-section-index`
- **Diagrams**: [Mermaid.js](https://mermaid.js.org/) injected via AST parsing
- **CI/CD**: GitHub Actions
- **Hosting**: GitHub Pages

## Project Structure

```text
├── .github/workflows/      # CI/CD Automation
├── backend/
│   └── app/                # Main Application Logic
│       ├── api/            # FastAPI Endpoints
│       ├── models/         # Pydantic Schemas (Data Layer)
│       └── services/       # Business Logic Layer
├── docs/                   # Static Markdown Documentation
├── scripts/                # The Automation Engine
│   ├── gen_ref_pages.py    # Generates the API Reference
│   ├── gen_architecture.py # AST-based architecture generator
│   ├── check_doc_sync.py   # Documentation integrity guard
│   └── run_pipeline.py     # Pipeline orchestrator
├── mkdocs.yml              # Documentation Configuration
└── requirements.txt        # Documentation Dependencies
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Pipeline**:
   ```bash
   python scripts/run_pipeline.py
   ```
3. **View the Site**: Open [http://127.0.0.1:8001/AutoCodeDoc/](http://127.0.0.1:8001/AutoCodeDoc/) in your browser.

## CI/CD & Hosting

This project is pre-configured to host on **GitHub Pages**.

- **Workflow**: Every push to `main` triggers an automated integrity check. If it passes, the site is built and deployed to your GitHub repository's `gh-pages` branch.
- **Live URL**: `https://koffandaff.github.io/AutoCodeDoc/`

---

*Built with ❤️ for automated, developer-first documentation.*
