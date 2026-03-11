"""
Unified Diagram Generator for AutoCodeDoc Platform
====================================================

Auto-generates all documentation diagrams from source code analysis:
- System Architecture diagram (from Python import graph via AST)
- ER Diagram (from Pydantic model introspection)
- Cross-Repo Data Flow (mllam-data-prep → weather-model-graphs → neural-lam)

All output is Mermaid.js format, embedded directly into Sphinx Markdown pages.

Usage
-----
    python scripts/generate_diagrams.py

Output
------
    docs/sphinx/architecture/system_diagram.md    (updated in-place)
    docs/sphinx/architecture/er_diagram.md        (updated in-place)
    docs/sphinx/architecture/cross_repo_flow.md   (updated in-place)
"""

import ast
import inspect
import importlib
import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

# ─── Path Setup ──────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
BACKEND_DIR = PROJECT_ROOT / "backend"
APP_DIR = BACKEND_DIR / "app"
SPHINX_DIR = PROJECT_ROOT / "docs"
ARCH_DIR = SPHINX_DIR / "architecture"

# Ensure backend is on sys.path for imports
sys.path.insert(0, str(BACKEND_DIR))


# ═══════════════════════════════════════════════════════════════════════════
# 1. SYSTEM ARCHITECTURE DIAGRAM — AST-based import graph
# ═══════════════════════════════════════════════════════════════════════════

def discover_modules(base_dir: Path) -> Dict[str, List[str]]:
    """
    Scan the backend for all API, Service, Model, and Utility files.

    Parameters
    ----------
    base_dir : Path
        Root directory of the application (e.g., ``backend/app``).

    Returns
    -------
    dict of str to list of str
        Mapping of layer name to list of module filenames (without .py).
    """
    components = {"api": [], "services": [], "models": [], "utils": [], "core": []}
    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".py") or file == "__init__.py":
                continue
            path = os.path.join(root, file)
            module_name = file.replace(".py", "")
            for layer in components:
                if os.sep + layer in path or f"/{layer}" in path:
                    components[layer].append(module_name)
                    break
    return components


def discover_import_connections(base_dir: Path) -> List[Tuple[str, str, str]]:
    """
    Parse Python imports to discover real connections between architectural layers.

    Uses AST (Abstract Syntax Tree) analysis to find ``from ... import ...``
    statements and map them to source→target connections.

    Parameters
    ----------
    base_dir : Path
        Root directory of the application.

    Returns
    -------
    list of tuple of (str, str, str)
        Each tuple is ``(source_id, target_id, connection_type)``.
    """
    connections = []
    layer_prefixes = {
        "api": "api_",
        "services": "svc_",
        "models": "mdl_",
        "utils": "utl_",
        "core": "core_",
    }

    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".py") or file == "__init__.py":
                continue
            filepath = os.path.join(root, file)
            source_name = file.replace(".py", "")

            # Determine source layer
            source_prefix = None
            for layer, prefix in layer_prefixes.items():
                if os.sep + layer in filepath or f"/{layer}" in filepath:
                    source_prefix = prefix
                    break
            if not source_prefix:
                continue

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())
            except (SyntaxError, UnicodeDecodeError):
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom) and node.module:
                    module_str = node.module
                    for target_layer, target_prefix in layer_prefixes.items():
                        if target_layer in module_str and target_prefix != source_prefix:
                            for alias in node.names:
                                if alias.name != "*":
                                    target_name = alias.name.lower()
                                    connections.append((
                                        f"{source_prefix}{source_name}",
                                        f"{target_prefix}{target_name}",
                                        f"{source_prefix.rstrip('_')}_to_{target_prefix.rstrip('_')}"
                                    ))
    return connections


def generate_system_architecture_mermaid(
    components: Dict[str, List[str]],
    connections: List[Tuple[str, str, str]]
) -> str:
    """
    Generate a Mermaid.js graph showing the system architecture.

    Parameters
    ----------
    components : dict
        Layer-to-modules mapping from :func:`discover_modules`.
    connections : list of tuple
        Import connections from :func:`discover_import_connections`.

    Returns
    -------
    str
        Complete Mermaid graph definition.
    """
    lines = [
        "graph TD",
        '    subgraph ClientLayer ["🌐 Client Layer"]',
        '        UI["Web Interface / API Consumer"]',
        "    end",
        "",
        '    subgraph APILayer ["🔌 API Layer (FastAPI Routes)"]',
        '        api_main["main.py"]',
    ]

    for api in sorted(components["api"]):
        lines.append(f'        api_{api}["{api}.py"]')
    lines.append("    end")
    lines.append("")

    lines.append('    subgraph ServiceLayer ["⚙️ Service Layer (Business Logic)"]')
    for service in sorted(components["services"]):
        lines.append(f'        svc_{service}["{service}.py"]')
    lines.append("    end")
    lines.append("")

    lines.append('    subgraph DataLayer ["💾 Data Layer (Pydantic Models)"]')
    for model in sorted(components["models"]):
        lines.append(f'        mdl_{model}["{model}.py"]')
    lines.append("    end")
    lines.append("")

    if components["utils"]:
        lines.append('    subgraph UtilsLayer ["🔧 Utilities"]')
        for util in sorted(components["utils"]):
            lines.append(f'        utl_{util}["{util}.py"]')
        lines.append("    end")
        lines.append("")

    if components["core"]:
        lines.append('    subgraph CoreLayer ["🏗️ Core"]')
        for core in sorted(components["core"]):
            lines.append(f'        core_{core}["{core}.py"]')
        lines.append("    end")
        lines.append("")

    # Client → Main → API routes
    lines.append("    UI --> api_main")
    for api in sorted(components["api"]):
        lines.append(f"    api_main --> api_{api}")

    # Real import-based connections
    connected_pairs: Set[Tuple[str, str]] = set()
    for source, target, _ in connections:
        pair = (source, target)
        if pair not in connected_pairs:
            connected_pairs.add(pair)
            lines.append(f"    {source} --> {target}")

    # Styling
    lines.extend([
        "",
        "    style ClientLayer fill:#e3f2fd,stroke:#1565c0",
        "    style APILayer fill:#e8f5e9,stroke:#2e7d32",
        "    style ServiceLayer fill:#fff3e0,stroke:#ef6c00",
        "    style DataLayer fill:#fce4ec,stroke:#c62828",
        "    style UtilsLayer fill:#f3e5f5,stroke:#7b1fa2",
        "    style CoreLayer fill:#e0f7fa,stroke:#00838f",
    ])

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════
# 2. ER DIAGRAM — From Pydantic model introspection
# ═══════════════════════════════════════════════════════════════════════════

def get_type_name(annotation) -> str:
    """
    Clean up complex Python type annotations for display.

    Parameters
    ----------
    annotation : type
        The type annotation to format.

    Returns
    -------
    str
        Human-readable type string.
    """
    try:
        if hasattr(annotation, "__name__"):
            return annotation.__name__
        type_str = str(annotation).replace("typing.", "")
        return type_str
    except Exception:
        return str(annotation)


def discover_pydantic_models(base_dir: Path) -> Tuple[Dict, List, Set[str]]:
    """
    Discover all Pydantic models, their fields, and relationships.

    Parameters
    ----------
    base_dir : Path
        Root directory to scan for model files.

    Returns
    -------
    tuple
        - entities: dict mapping model name → list of ``(type, field_name)``
        - relationships: list of ``(parent, child, rel_type, field_name)``
        - model_names: set of all discovered model names
    """
    from pydantic import BaseModel

    entities: Dict[str, List[Tuple[str, str]]] = {}
    relationships: List[Tuple[str, str, str, str]] = []
    model_names: Set[str] = set()

    # First pass: collect all model names
    for path in sorted(base_dir.rglob("*.py")):
        if "models" not in path.parts:
            continue
        try:
            module_parts = list(path.with_suffix("").parts)
            app_idx = module_parts.index("app")
            ident = ".".join(module_parts[app_idx:])
            module = importlib.import_module(ident)
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and issubclass(obj, BaseModel)
                        and obj is not BaseModel
                        and getattr(obj, "__module__", "") == module.__name__):
                    model_names.add(name)
        except Exception:
            continue

    # Second pass: collect fields and relationships
    for path in sorted(base_dir.rglob("*.py")):
        if "models" not in path.parts:
            continue
        try:
            module_parts = list(path.with_suffix("").parts)
            app_idx = module_parts.index("app")
            ident = ".".join(module_parts[app_idx:])
            module = importlib.import_module(ident)

            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and issubclass(obj, BaseModel)
                        and obj is not BaseModel
                        and getattr(obj, "__module__", "") == module.__name__):
                    attributes = []
                    for field_name, field in obj.model_fields.items():
                        type_name = get_type_name(field.annotation)
                        safe_type = "".join(
                            c for c in type_name.replace("[", "_").replace("]", "")
                            .replace(",", "_").replace(" ", "")
                            if c.isalnum() or c == "_"
                        ) or "any"
                        attributes.append((safe_type, field_name))

                        # Detect relationships
                        annot_str = str(field.annotation)
                        for other_name in model_names:
                            if other_name in annot_str and other_name != name:
                                relationships.append(
                                    (name, other_name, "||--o{", field_name)
                                )

                    entities[name] = attributes
        except Exception:
            continue

    return entities, relationships, model_names


def generate_er_mermaid(
    entities: Dict[str, List[Tuple[str, str]]],
    relationships: List[Tuple[str, str, str, str]]
) -> str:
    """
    Generate a Mermaid.js erDiagram from discovered Pydantic models.

    Parameters
    ----------
    entities : dict
        Model name → list of ``(type, field_name)`` tuples.
    relationships : list of tuple
        ``(parent, child, rel_type, field_name)`` tuples.

    Returns
    -------
    str
        Complete Mermaid erDiagram definition.
    """
    lines = ["erDiagram"]

    for entity, attributes in sorted(entities.items()):
        lines.append(f"    {entity} {{")
        for type_name, field_name in attributes:
            lines.append(f"        {type_name} {field_name}")
        lines.append("    }")

    # Deduplicate relationships
    seen = set()
    for parent, child, rel, field in sorted(relationships):
        key = (parent, child)
        if key not in seen:
            seen.add(key)
            lines.append(f'    {parent} {rel} {child} : "via {field}"')

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════
# 3. CROSS-REPO DATA FLOW DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════

def generate_cross_repo_flow() -> str:
    """
    Generate a Mermaid.js data flow diagram showing how the three
    neural-lam ecosystem repositories interact.

    Returns
    -------
    str
        Mermaid flowchart definition.

    Notes
    -----
    The three repos in the pipeline are:

    - **mllam-data-prep**: Generates ``.zarr`` datasets consumed by neural-lam
      via ``MDPDatastore``
    - **weather-model-graphs**: Generates ``.pt`` graph files consumed by neural-lam
    - **neural-lam**: Core training engine that consumes both data sources
    """
    return """graph LR
    subgraph mllam_data_prep ["📦 mllam-data-prep"]
        MDP_CONFIG["config.yaml\\n(data sources, variables)"]
        MDP_PROCESS["Data Processing\\n(xarray/dask)"]
        MDP_OUTPUT[".zarr Dataset\\n(standardized weather data)"]
        MDP_CONFIG --> MDP_PROCESS --> MDP_OUTPUT
    end

    subgraph weather_model_graphs ["🌐 weather-model-graphs"]
        WMG_CONFIG["graph_config.yaml\\n(mesh topology)"]
        WMG_BUILD["Graph Builder\\n(networkx)"]
        WMG_OUTPUT[".pt Graph Files\\n(mesh, g2m, m2g edges)"]
        WMG_CONFIG --> WMG_BUILD --> WMG_OUTPUT
    end

    subgraph neural_lam ["🧠 neural-lam"]
        NL_DATASTORE["MDPDatastore\\n(reads .zarr)"]
        NL_GRAPH["Graph Loading\\n(reads .pt files)"]
        NL_MODEL["GNN Model\\n(Hi-LAM / GraphLAM)"]
        NL_TRAIN["Training Loop\\n(PyTorch Lightning)"]
        NL_EVAL["Evaluation\\n(RMSE, MAE, ACC)"]

        NL_DATASTORE --> NL_MODEL
        NL_GRAPH --> NL_MODEL
        NL_MODEL --> NL_TRAIN
        NL_TRAIN --> NL_EVAL
    end

    MDP_OUTPUT -->|".zarr via\\nMDPDatastore"| NL_DATASTORE
    WMG_OUTPUT -->|".pt graph\\nfiles"| NL_GRAPH

    style mllam_data_prep fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style weather_model_graphs fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style neural_lam fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style MDP_OUTPUT fill:#bbdefb,stroke:#1565c0
    style WMG_OUTPUT fill:#c8e6c9,stroke:#2e7d32
    style NL_MODEL fill:#ffe0b2,stroke:#ef6c00
    style NL_EVAL fill:#ffccbc,stroke:#bf360c"""


# ═══════════════════════════════════════════════════════════════════════════
# 4. WRITE OUTPUT FILES
# ═══════════════════════════════════════════════════════════════════════════

def write_system_architecture_page(mermaid_content: str, components: Dict) -> None:
    """
    Write the system architecture documentation page.

    Parameters
    ----------
    mermaid_content : str
        Generated Mermaid graph.
    components : dict
        Discovered module components for the summary table.
    """
    os.makedirs(ARCH_DIR, exist_ok=True)

    total_modules = sum(len(v) for v in components.values())

    content = f"""# System Architecture Diagram

> **Auto-generated** from Python import graph analysis (AST-based).
> Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

This diagram shows the complete system architecture of the AutoCodeDoc Platform,
with connections discovered by parsing Python `import` statements across {total_modules} modules.

```{{mermaid}}
{mermaid_content}
```

## Module Summary

| Layer | Count | Modules |
|-------|-------|---------|
| API Routes | {len(components['api'])} | {', '.join(f'`{m}`' for m in sorted(components['api'])) or '*none*'} |
| Services | {len(components['services'])} | {', '.join(f'`{m}`' for m in sorted(components['services'])) or '*none*'} |
| Models | {len(components['models'])} | {', '.join(f'`{m}`' for m in sorted(components['models'])) or '*none*'} |
| Utilities | {len(components['utils'])} | {', '.join(f'`{m}`' for m in sorted(components['utils'])) or '*none*'} |
| Core | {len(components['core'])} | {', '.join(f'`{m}`' for m in sorted(components['core'])) or '*none*'} |

## How It Works

The diagram above is generated automatically by the `generate_diagrams.py` script:

1. **Module Discovery**: Walks the `backend/app/` directory tree and categorizes files by layer
2. **Import Analysis**: Parses each `.py` file's AST to find `from ... import ...` statements
3. **Connection Mapping**: Maps imports to source→target connections between layers
4. **Mermaid Generation**: Converts the graph into a Mermaid.js flowchart

No manual editing required. Just run:

```bash
python scripts/generate_diagrams.py
```
"""
    with open(ARCH_DIR / "system_diagram.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ System architecture → {ARCH_DIR / 'system_diagram.md'}")


def write_er_diagram_page(
    mermaid_content: str,
    entities: Dict,
    relationships: List
) -> None:
    """
    Write the ER diagram documentation page.

    Parameters
    ----------
    mermaid_content : str
        Generated Mermaid erDiagram.
    entities : dict
        Discovered Pydantic model entities.
    relationships : list
        Discovered inter-model relationships.
    """
    os.makedirs(ARCH_DIR, exist_ok=True)

    total_fields = sum(len(attrs) for attrs in entities.values())

    content = f"""# Entity-Relationship Diagram

> **Auto-generated** from Pydantic model introspection.
> Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

This ER diagram is built dynamically by scanning all Pydantic `BaseModel` subclasses,
extracting their fields (names, types, validators), and detecting relationships between models.

- **{len(entities)}** entities discovered
- **{total_fields}** total fields
- **{len(set((r[0], r[1]) for r in relationships))}** relationships detected

```{{mermaid}}
{mermaid_content}
```

## Entity Details

"""
    for entity, attributes in sorted(entities.items()):
        content += f"### {entity}\n\n"
        content += "| Field | Type |\n"
        content += "|-------|------|\n"
        for type_name, field_name in attributes:
            content += f"| `{field_name}` | `{type_name}` |\n"
        content += "\n"

    if relationships:
        content += "## Relationships\n\n"
        content += "| Parent | → | Child | Via Field |\n"
        content += "|--------|---|-------|-----------|\n"
        seen = set()
        for parent, child, _, field in sorted(relationships):
            key = (parent, child)
            if key not in seen:
                seen.add(key)
                content += f"| `{parent}` | → | `{child}` | `{field}` |\n"
        content += "\n"

    content += """## How It Works

The ER diagram is generated by `generate_diagrams.py`:

1. **Model Discovery**: Finds all classes inheriting from `pydantic.BaseModel`
2. **Field Extraction**: Reads `model_fields` for names, types, and annotations
3. **Relationship Detection**: Checks if any field's type annotation references another model
4. **Mermaid Generation**: Converts entities and relationships into a Mermaid erDiagram
"""

    with open(ARCH_DIR / "er_diagram.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ ER diagram → {ARCH_DIR / 'er_diagram.md'}")


def write_cross_repo_flow_page(mermaid_content: str) -> None:
    """
    Write the cross-repo data flow documentation page.

    Parameters
    ----------
    mermaid_content : str
        Generated Mermaid data flow diagram.
    """
    os.makedirs(ARCH_DIR, exist_ok=True)

    content = f"""# Cross-Repository Data Flow

> **Auto-generated** pipeline visualization showing how the three neural-lam
> ecosystem repositories interact.
> Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## The Three-Repo Pipeline

The neural-lam ecosystem consists of three interconnected repositories that form
a complete weather prediction pipeline:

| Repository | Purpose | Output |
|------------|---------|--------|
| [mllam-data-prep](https://github.com/mllam/mllam-data-prep) | Data preprocessing | `.zarr` datasets |
| [weather-model-graphs](https://github.com/mllam/weather-model-graphs) | Graph topology | `.pt` graph files |
| [neural-lam](https://github.com/mllam/neural-lam) | Model training & eval | Trained weights |

## Data Flow Diagram

```{{mermaid}}
{mermaid_content}
```

## Pipeline Details

### 1. mllam-data-prep → `.zarr` Datasets

The `mllam-data-prep` repository processes raw weather data (e.g., ERA5, DANRA)
into standardized `.zarr` datasets. It:

- Reads configuration from `config.yaml` defining data sources and variables
- Uses `xarray` and `dask` for parallel data processing
- Outputs `.zarr` stores with consistent coordinate systems and variable naming

### 2. weather-model-graphs → `.pt` Graph Files

The `weather-model-graphs` repository generates the graph structures used by
the neural-lam GNN models:

- **Mesh graphs**: Define the internal model resolution hierarchy
- **Grid-to-Mesh (g2m)**: Map input grid points to mesh nodes
- **Mesh-to-Grid (m2g)**: Map mesh predictions back to output grid

### 3. neural-lam — Core Training Engine

The `neural-lam` repository is the core training engine that:

- Loads `.zarr` data via `MDPDatastore` (from mllam-data-prep output)
- Loads `.pt` graph files (from weather-model-graphs output)
- Trains Graph Neural Network models (Hi-LAM, GraphLAM)
- Evaluates predictions using RMSE, MAE, and ACC metrics

## Integration Points

```{{mermaid}}
graph TD
    A["mllam-data-prep\\nconfig.yaml"] -->|"creates"| B[".zarr store"]
    C["weather-model-graphs\\ngraph_config.yaml"] -->|"creates"| D[".pt files"]
    B -->|"imported via"| E["neural_lam.weather_dataset\\nMDPDatastore"]
    D -->|"loaded in"| F["neural_lam.models\\ngraph loading"]
    E --> G["Training Pipeline"]
    F --> G
    G --> H["Evaluation Metrics"]
    H --> I["Trained Model Weights"]

    style A fill:#e3f2fd
    style C fill:#e8f5e9
    style G fill:#fff3e0
    style I fill:#ffccbc
```

## See Also

- [System Architecture](system_diagram.md) — Internal module architecture
- [ER Diagram](er_diagram.md) — Data model relationships
"""

    with open(ARCH_DIR / "cross_repo_flow.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ Cross-repo flow → {ARCH_DIR / 'cross_repo_flow.md'}")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def generate_all_diagrams() -> Dict:
    """
    Generate all documentation diagrams and return a summary report.

    Returns
    -------
    dict
        Summary report with counts of entities, connections, and files generated.
    """
    print("🔍 Scanning codebase for diagram generation...\n")

    # 1. System Architecture
    print("📐 Generating System Architecture Diagram...")
    components = discover_modules(APP_DIR)
    connections = discover_import_connections(APP_DIR)
    sys_mermaid = generate_system_architecture_mermaid(components, connections)
    write_system_architecture_page(sys_mermaid, components)

    # 2. ER Diagram
    print("\n📊 Generating ER Diagram...")
    entities, relationships, model_names = discover_pydantic_models(APP_DIR)
    er_mermaid = generate_er_mermaid(entities, relationships)
    write_er_diagram_page(er_mermaid, entities, relationships)

    # 3. Cross-Repo Data Flow
    print("\n🌐 Generating Cross-Repo Data Flow Diagram...")
    cross_repo = generate_cross_repo_flow()
    write_cross_repo_flow_page(cross_repo)

    # Summary
    report = {
        "timestamp": datetime.now().isoformat(),
        "diagrams_generated": 3,
        "system_architecture": {
            "total_modules": sum(len(v) for v in components.values()),
            "connections": len(connections),
            "layers": {k: len(v) for k, v in components.items()},
        },
        "er_diagram": {
            "entities": len(entities),
            "total_fields": sum(len(attrs) for attrs in entities.values()),
            "relationships": len(set((r[0], r[1]) for r in relationships)),
        },
        "cross_repo_flow": {
            "repos": ["mllam-data-prep", "weather-model-graphs", "neural-lam"],
        },
    }

    print(f"\n{'─' * 60}")
    print(f"✅ ALL DIAGRAMS GENERATED SUCCESSFULLY")
    print(f"   System Architecture: {report['system_architecture']['total_modules']} modules, {report['system_architecture']['connections']} connections")
    print(f"   ER Diagram: {report['er_diagram']['entities']} entities, {report['er_diagram']['total_fields']} fields")
    print(f"   Cross-Repo Flow: {len(report['cross_repo_flow']['repos'])} repositories")
    print(f"{'─' * 60}")

    return report


if __name__ == "__main__":
    report = generate_all_diagrams()
    # Save report as JSON for CI/CD consumption
    report_path = PROJECT_ROOT / "diagrams_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\n📄 Report saved to {report_path}")
