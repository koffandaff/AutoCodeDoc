# Changelog

All notable changes to the AutoCodeDoc Platform will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-03-11

### Added

- **Sphinx + AutoAPI** as primary documentation engine
  - Fully automated API reference generation via `sphinx-autoapi`
  - NumPy-style docstring support via Napoleon
  - Mermaid.js diagram rendering via `sphinxcontrib-mermaid`
  - Cross-repo intersphinx linking
  - Responsive RTD theme with custom CSS

- **Architecture Diagrams** (auto-generated)
  - System architecture from Python import graph (AST-based)
  - ER diagrams from Pydantic model introspection
  - Cross-repo data flow (mllam-data-prep → weather-model-graphs → neural-lam)

- **ML/LLM Documentation Sections**
  - Model architecture visualization
  - Training data pipeline documentation
  - Hyperparameter schema extraction
  - Evaluation metrics structure

- **Quality & CI/CD**
  - `interrogate` integration for non-blocking docstring coverage
  - Unified `run_pipeline.py` for single-command builds
  - `docs_report.json` feedback artifact after every build
  - GitHub Actions workflow with lint → coverage → build → deploy

- **Backend Test Suite**
  - `test_docs_build.py` — Sphinx build validation
  - `test_coverage.py` — Docstring coverage via interrogate
  - `test_diagrams.py` — Diagram output validation
  - `test_autoapi.py` — AutoAPI index verification

- **Static Content Pages**
  - Installation guide with environment setup
  - End-to-end usage walkthrough
  - Contributing guide with NumPy docstring templates
  - This changelog

### Changed

- MkDocs demoted to secondary documentation at `/legacy-docs/`
- Napoleon config switched from Google-style to NumPy-style
- `requirements.txt` updated with all Sphinx and quality tooling

### Preserved

- Full MkDocs site functionality (additive change only)
- All existing documented items (endpoints, schemas, services, utilities)
- GitHub Pages deployment via `peaceiris/actions-gh-pages`

## [0.1.0] — 2026-03-09

### Added

- Initial MkDocs + Material theme setup
- Custom AST-based architecture diagram generation
- Pydantic field description integrity checker
- `mkdocstrings` for API reference from Google-style docstrings
- Basic Sphinx setup in `docs_sphinx/` with `sphinx-rtd-theme`
- GitHub Actions CI/CD for MkDocs deployment
