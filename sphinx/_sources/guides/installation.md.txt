# Installation Guide

## Prerequisites

Before installing the AutoCodeDoc Platform, ensure you have:

- **Python 3.10+** — [Download Python](https://www.python.org/downloads/)
- **pip** — Comes bundled with Python 3.4+
- **Git** — [Download Git](https://git-scm.com/downloads)
- **Graphviz** *(optional, for SVG diagram export)* — [Download Graphviz](https://graphviz.org/download/)

## Quick Install

### 1. Clone the Repository

```bash
git clone https://github.com/koffandaff/AutoCodeDoc.git
cd AutoCodeDoc/doc_automation_platform
```

### 2. Create a Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs everything needed for both documentation engines:

| Package              | Purpose                                      |
|----------------------|----------------------------------------------|
| `sphinx`             | Primary documentation engine                 |
| `sphinx-autoapi`     | Auto-generates API docs from source code     |
| `sphinxcontrib-mermaid` | Renders Mermaid.js diagrams in Sphinx     |
| `sphinx-design`      | Cards, grids, tabs for rich layouts          |
| `interrogate`        | Docstring coverage analysis                  |
| `mkdocs-material`    | Secondary MkDocs site (legacy)               |
| `mkdocstrings`       | MkDocs Python doc renderer                   |

### 4. Verify Installation

```bash
# Check Sphinx
sphinx-build --version

# Check interrogate
interrogate --version

# Check all imports work
python -c "import sphinx, autoapi, sphinxcontrib.mermaid; print('All good!')"
```

## Environment Setup

### Environment Variables

| Variable       | Default                | Description                          |
|----------------|------------------------|--------------------------------------|
| `PYTHONPATH`   | `./backend`            | Required for autoapi module discovery|
| `DOCS_OUTPUT`  | `./site`               | Where built docs are written         |

Set these in your shell or `.env` file:

```bash
export PYTHONPATH="$PWD/backend"
export DOCS_OUTPUT="$PWD/site"
```

### IDE Integration

For **VS Code**, add to `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": ["./backend"],
    "python.formatting.provider": "black",
    "restructuredtext.confPath": "${workspaceFolder}/doc_automation_platform/docs/sphinx"
}
```

## Building Documentation

### Single Command (Recommended)

```bash
python run_pipeline.py
```

This runs the full pipeline: lint → coverage check → diagram generation → Sphinx build → optional serve.

### Manual Build

```bash
# Sphinx only
cd docs/sphinx
sphinx-build -b html . ../../site/sphinx

# MkDocs only
mkdocs build -d site
```

## Troubleshooting

```{admonition} Common Issues
:class: tip

- **ModuleNotFoundError**: Ensure `PYTHONPATH` includes the `backend/` directory
- **Mermaid not rendering**: Check that `sphinxcontrib-mermaid` is installed
- **AutoAPI shows no modules**: Verify `autoapi_dirs` in `conf.py` points to valid Python packages
```

## Next Steps

- Read the [Usage Guide](usage.md) for an end-to-end walkthrough
- Explore the [Architecture Diagrams](../architecture/system_diagram.md)
- Browse the [API Reference](../api/index.rst)
