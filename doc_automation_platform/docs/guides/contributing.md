# Contributing Guide

Thank you for considering contributing to AutoCodeDoc! This guide covers docstring standards, development workflow, and how to submit your changes.

## Docstring Standard: NumPy Style

All code in this project **must** use [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html). This ensures consistent, machine-readable documentation that Sphinx can render automatically.

### Required Sections

Every public function, class, and method must include:

| Section       | Required? | Description                                    |
|---------------|-----------|------------------------------------------------|
| Summary       | ✅ Yes    | One-line description of what it does            |
| Parameters    | ✅ Yes    | All parameters with types and descriptions      |
| Returns       | ✅ Yes    | Return value with type and description          |
| Raises        | If applicable | Exceptions that can be raised               |
| Examples      | Encouraged | Usage examples with expected output            |
| Notes         | Optional  | Implementation notes or caveats                 |
| See Also      | Optional  | Links to related functions/classes              |

### Template

```python
def process_data(input_data: dict, validate: bool = True) -> dict:
    """
    Process incoming data through the transformation pipeline.

    Takes raw input data, applies validation and normalization steps,
    and returns the processed result ready for downstream consumption.

    Parameters
    ----------
    input_data : dict
        The raw data dictionary to process. Must contain at minimum
        a ``"type"`` key indicating the data category.
    validate : bool, optional
        Whether to run validation checks before processing.
        Default is True.

    Returns
    -------
    dict
        The processed data with normalized keys and validated values.

    Raises
    ------
    ValueError
        If ``input_data`` is empty or missing required keys.
    TypeError
        If ``input_data`` is not a dictionary.

    Examples
    --------
    >>> result = process_data({"type": "user", "name": "Alice"})
    >>> print(result["status"])
    'processed'

    See Also
    --------
    validate_data : Validation step used internally.
    normalize_keys : Key normalization utility.
    """
    ...
```

### Pydantic Model Docstrings

For Pydantic models, use **both** class docstrings and `Field(description=...)`:

```python
class UserCreate(BaseModel):
    """
    Model used to create a new user account.

    Attributes
    ----------
    username : str
        The desired username (3-50 characters).
    email : str
        A valid email address for the account.
    bio : str, optional
        A short biography for the user profile.
    """

    username: str = Field(description="The desired username (3-50 characters).")
    email: str = Field(description="A valid email address for the account.")
    bio: Optional[str] = Field(default=None, description="A short biography for the user profile.")
```

## Development Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/AutoCodeDoc.git
cd AutoCodeDoc/doc_automation_platform
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes

- Write code with NumPy-style docstrings
- Add `Field(description=...)` to all Pydantic fields
- Keep functions focused and well-documented

### 4. Check Coverage Before Committing

```bash
# Check docstring coverage
interrogate backend/ -v --fail-under 90

# Run the full pipeline
python run_pipeline.py --build-only
```

### 5. Submit a Pull Request

- Ensure all docstring coverage checks pass
- Verify Sphinx builds without warnings
- Include a clear description of your changes
- Reference any related issues

## Code Style

| Rule                    | Standard                                    |
|-------------------------|---------------------------------------------|
| Docstring format        | NumPy-style                                 |
| Type hints              | Required on all public functions             |
| Line length             | 100 characters max                          |
| Imports                 | Sorted with `isort`                         |
| Formatting              | `black` with default settings               |

## CI/CD Pipeline

When you push to `main` or open a PR, the CI pipeline automatically:

1. **Lints** the codebase for syntax errors
2. **Checks docstring coverage** with `interrogate` (non-blocking — warns but doesn't fail)
3. **Builds Sphinx documentation** and checks for warnings
4. **Deploys** to GitHub Pages (on merge to `main`)

```{admonition} Important
:class: warning

The docstring coverage check is **non-blocking** by design. It will comment on your PR if coverage drops, but it won't prevent merging. This is intentional — we want to track coverage trends without blocking development.
```

## Adding New Modules

When adding a new module to the backend:

1. Create the file in the appropriate directory (`api/`, `services/`, `models/`, `utils/`)
2. Add an `__init__.py` if creating a new package
3. Write complete NumPy-style docstrings for all public items
4. Run `python run_pipeline.py --build-only` to verify it appears in the API Reference
5. The ER diagram and system architecture will update automatically

## Questions?

- Open a [GitHub Issue](https://github.com/koffandaff/AutoCodeDoc/issues)
- Check the [Usage Guide](usage.md) for workflow details
- Review the [API Reference](../api/index.rst) for existing patterns
