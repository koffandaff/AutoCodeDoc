# Usage Guide

This guide walks you through the full documentation workflow — from writing docstrings to deploying a production-ready documentation site.

## End-to-End Workflow

```{mermaid}
graph LR
    A["Write Code + Docstrings"] --> B["Run Pipeline"]
    B --> C["Diagrams Generated"]
    B --> D["Coverage Checked"]
    B --> E["Sphinx Build"]
    E --> F["Deploy to GitHub Pages"]
    D --> G["docs_report.json"]
    style A fill:#4051b5,color:#fff
    style F fill:#4caf50,color:#fff
    style G fill:#ff9800,color:#fff
```

## Step 1: Write NumPy-Style Docstrings

All documentation is extracted from your source code. Use **NumPy-style** docstrings throughout:

### For Functions

```python
async def fetch_user_by_id(user_id: int) -> Optional[User]:
    """
    Retrieve a user from the database by their unique ID.

    Parameters
    ----------
    user_id : int
        The unique identifier of the user to retrieve.

    Returns
    -------
    Optional[User]
        The user object if found, otherwise None.

    Raises
    ------
    HTTPException
        If the user does not exist (404).

    Examples
    --------
    >>> user = await fetch_user_by_id(42)
    >>> print(user.username)
    'johndoe'
    """
    return await db.get(user_id)
```

### For Pydantic Models

```python
class User(BaseModel):
    """
    User model representing an account in the system.

    Attributes
    ----------
    id : int
        The unique identifier for the user.
    username : str
        The login username.
    email : str
        The email address of the user.
    """

    id: int = Field(description="The unique identifier for the user.")
    username: str = Field(description="The login username.")
    email: str = Field(description="The email address of the user.")
```

## Step 2: Run the Pipeline

```bash
# Full pipeline (lint → coverage → diagrams → build → serve)
python run_pipeline.py

# Build only (no server)
python run_pipeline.py --build-only

# Skip coverage check (faster iteration)
python run_pipeline.py --skip-coverage
```

### What Happens

1. **Lint Check** — Validates Python syntax across the backend
2. **Interrogate Coverage** — Reports docstring coverage percentage (non-blocking)
3. **Diagram Generation** — AST-parses your code to produce Mermaid diagrams
4. **Sphinx Build** — Compiles all docs into a static HTML site
5. **Report Generation** — Creates `docs_report.json` with build metadata

## Step 3: Review the Output

After the pipeline completes, you'll find:

| Output                    | Location                      | Description                           |
|---------------------------|-------------------------------|---------------------------------------|
| Sphinx HTML site          | `site/sphinx/`                | Primary documentation site            |
| MkDocs HTML site          | `site/`                       | Legacy MkDocs documentation           |
| Build report              | `docs_report.json`            | Modules, coverage, diagrams, warnings |
| API reference             | `site/sphinx/api/`            | Auto-generated from source            |

## Step 4: Explore the Live Site

Open your browser to view the documentation:

```bash
# Sphinx (primary) — opens automatically with run_pipeline.py
http://127.0.0.1:8002

# MkDocs (secondary)
http://127.0.0.1:8001
```

## Common Workflows

### Adding a New API Endpoint

1. Create the endpoint in `backend/app/api/`
2. Add NumPy-style docstrings with Parameters, Returns, Raises
3. Run `python run_pipeline.py --build-only`
4. Verify the endpoint appears in the API Reference

### Adding a New Pydantic Model

1. Define the model in `backend/app/models/`
2. Add `Field(description="...")` to every field
3. Run the pipeline — the ER diagram and schema pages update automatically

### Checking Docstring Coverage

```bash
# Quick check
interrogate backend/ -v

# With badge generation
interrogate backend/ -v --generate-badge docs/sphinx/_static/
```

## Architecture of the Doc System

```{mermaid}
graph TD
    subgraph Sources["Source Code"]
        PY["Python Modules"]
        DS["NumPy Docstrings"]
        PM["Pydantic Models"]
    end

    subgraph Engine["Documentation Engine"]
        AA["sphinx-autoapi"]
        NAP["napoleon"]
        MER["sphinxcontrib-mermaid"]
        GEN["generate_diagrams.py"]
    end

    subgraph Output["Generated Docs"]
        API["API Reference"]
        ARCH["Architecture Diagrams"]
        ER["ER Diagrams"]
        FLOW["Data Flow"]
    end

    PY --> AA
    DS --> NAP
    PM --> GEN
    PY --> GEN
    AA --> API
    NAP --> API
    MER --> ARCH
    GEN --> ER
    GEN --> FLOW

    style Sources fill:#e8eaf6
    style Engine fill:#fff3e0
    style Output fill:#e8f5e9
```

## Next Steps

- Review the [Architecture Diagrams](../architecture/system_diagram.md)
- Read the [Contributing Guide](contributing.md) to learn the doc standards
