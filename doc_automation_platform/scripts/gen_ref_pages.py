"""Generate the code reference pages and Platform Overview."""

import mkdocs_gen_files
from pathlib import Path
import sys
import os
import ast
import inspect
import importlib
from pydantic import BaseModel
from pydantic_core import PydanticUndefined

nav = mkdocs_gen_files.Nav()

def get_type_name(annotation):
    """Clean up complex type names for documentation."""
    try:
        if hasattr(annotation, "__name__"):
            return annotation.__name__
        type_str = str(annotation).replace("typing.", "")
        return type_str
    except:
        return str(annotation)

def get_function_summary(filepath: str) -> list:
    """Parse a Python file and extract function names and their first docstring line."""
    results = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                summary = ""
                docstring = ast.get_docstring(node)
                if docstring:
                    summary = docstring.strip().split("\n")[0]
                # Build arg list
                args = []
                for arg in node.args.args:
                    if arg.arg != "self":
                        args.append(arg.arg)
                sig = f"{node.name}({', '.join(args)})"
                results.append({"name": node.name, "sig": sig, "summary": summary, "is_async": isinstance(node, ast.AsyncFunctionDef)})
    except:
        pass
    return results

# Collections for consolidated views
all_model_tables = []
all_services = []          # (display_name, module_ident)
all_routers = []           # (display_name, module_ident)
all_relationships = []     # (Parent, Child, RelationType)
all_api_summaries = []     # Rich API endpoint summaries
all_service_summaries = [] # Rich service function summaries
global_models = set()

src = Path("backend/app")

# Ensure backend is in path for imports
backend_path = Path("backend").absolute()
if str(backend_path) not in sys.path:
    sys.path.append(str(backend_path))

# PRE-PASS: Collect all model names globally
for path in sorted(src.rglob("*.py")):
    if "models" in path.parts:
        try:
            module_parts = list(path.with_suffix("").parts)
            app_idx = module_parts.index("app")
            ident = ".".join(module_parts[app_idx:])
            module = importlib.import_module(ident)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj != BaseModel and getattr(obj, "__module__", "") == module.__name__:
                    global_models.add(name)
        except:
            continue

# ─── MAIN LOOP: Generate per-module reference pages ─────────────────────
for path in sorted(src.rglob("*.py")):
    module_parts = list(path.with_suffix("").parts)
    
    try:
        app_idx = module_parts.index("app")
        parts = tuple(module_parts[app_idx:])
    except ValueError:
        continue

    full_doc_path = Path(*parts).with_suffix(".md")
    doc_path = Path(*parts).with_suffix(".md")

    is_init = (parts[-1] == "__init__")
    
    if is_init:
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "main":
        pass

    ident = ".".join(parts)
    
    # Collect services and routers (skip __init__ files)
    if "services" in parts and not is_init:
        display = parts[-1].replace("_", " ").title()
        all_services.append((display, ident))
        # Extract function summaries for the Features page
        funcs = get_function_summary(str(path))
        all_service_summaries.append({"name": display, "ident": ident, "functions": funcs})
        
    if "api" in parts and not is_init:
        display = parts[-1].replace("_", " ").title()
        all_routers.append((display, ident))
        funcs = get_function_summary(str(path))
        all_api_summaries.append({"name": display, "ident": ident, "functions": funcs})

    # Navigation mapping
    nav_parts = list(parts)
    if "models" in nav_parts:
        nav_parts[nav_parts.index("models")] = "Schema"
    nav[tuple(nav_parts)] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        fd.write(f"# {ident}\n\n::: {ident}\n\n")
        
        # If this is a model file, add a dynamic schema table
        if "models" in parts:
            try:
                module = importlib.import_module(ident)
                
                f_header_written = False
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj != BaseModel and getattr(obj, "__module__", "") == module.__name__:
                        if not f_header_written:
                            fd.write("## Database Fields\n\nDetailed breakdown for this model file.\n\n")
                            f_header_written = True
                        
                        table_content = f"### Entity: {name}\n\n"
                        table_content += f"{obj.__doc__ or ''}\n\n"
                        table_content += "| Field | Type | Description | Default |\n"
                        table_content += "|-------|------|-------------|---------|\n"
                        
                        for field_name, field in obj.model_fields.items():
                            type_name = get_type_name(field.annotation)
                            desc = field.description or "*(No description provided)*"
                            
                            default_val = field.default
                            if default_val is PydanticUndefined:
                                if field.default_factory:
                                    default_str = f"`{field.default_factory.__name__}()`"
                                else:
                                    default_str = "*Required*"
                            elif default_val is None:
                                default_str = "`None`"
                            else:
                                default_str = f"`{default_val}`"
                            
                            table_content += f"| `{field_name}` | `{type_name}` | {desc} | {default_str} |\n"
                            
                            # Relationship Detection
                            annot_str = str(field.annotation)
                            for other_name in global_models:
                                if other_name in annot_str and other_name != name:
                                    all_relationships.append((name, other_name, "||--o{"))

                        table_content += "\n"
                        fd.write(table_content)
                        all_model_tables.append(table_content)
            except Exception as e:
                fd.write(f"\n> [!CAUTION]\n> **Auto-Schema Error**: Could not generate tables for {ident}. Error: `{str(e)}`")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

# ─── NEW ER DIAGRAM GENERATION ──────────────────────────────────────────
all_er_entities = {} # name -> attributes list
all_er_relationships = []

# Collect ER entities and relationships safely
for path in sorted(src.rglob("*.py")):
    if "models" not in path.parts:
        continue
        
    module_parts = list(path.with_suffix("").parts)
    try:
        app_idx = module_parts.index("app")
        ident = ".".join(module_parts[app_idx:])
        module = importlib.import_module(ident)
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj != BaseModel and getattr(obj, "__module__", "") == module.__name__:
                attributes = []
                for field_name, field in obj.model_fields.items():
                    type_name = get_type_name(field.annotation)
                    # Clean type name for Mermaid
                    safe_type = type_name.replace("[", "_").replace("]", "").replace(",", "_").replace(" ", "")
                    # Strip any non-alphanumeric chars except underscore
                    safe_type = "".join(c for c in safe_type if c.isalnum() or c == "_")
                    if not safe_type:
                        safe_type = "any"
                    attributes.append(f"{safe_type} {field_name}")
                    
                    # Detect relationships
                    annot_str = str(field.annotation)
                    for other_name in global_models:
                        if other_name in annot_str and other_name != name:
                            all_er_relationships.append((name, other_name, "||--o{", field_name))
                
                all_er_entities[name] = attributes
    except:
        pass
nav["Home"] = "index.md"
nav["System Overview"] = "architecture.md"
nav["Installation"] = "installation.md"
nav["Usage Guide"] = "usage.md"
nav["Navigation Test"] = "test.md"
nav["Contributing"] = "contributing.md"

nav["Platform Overview", "Features Connection"] = "design/features.md"
nav["Platform Overview", "System Diagrams"] = "design/diagrams.md"
nav["Platform Overview", "API Routes Listing"] = "design/routes.md"
nav["Platform Overview", "Database Schema"] = "design/schema.md"

# ─── 1. DATABASE SCHEMA (Consolidated Tables + erDiagram) ──────────────
with mkdocs_gen_files.open("design/schema.md", "w") as f:
    f.write("# Database Schema\n\n")
    f.write("Comprehensive breakdown of all platform data models, auto-generated from Pydantic source code.\n\n")
    
    f.write("## Entity-Relationship Diagram\n\n")
    f.write("This true ER diagram is built dynamically by scanning all database models and their fields.\n\n")
    
    f.write("```mermaid\nerDiagram\n")
    # Write entities
    for entity, attributes in sorted(all_er_entities.items()):
        f.write(f"    {entity} {{\n")
        for attr in attributes:
            f.write(f"        {attr}\n")
        f.write("    }\n")
    
    # Write relationships
    for parent, child, rel, field in sorted(list(set(all_er_relationships))):
        f.write(f"    {parent} {rel} {child} : \"contains/references\"\n")
    f.write("```\n\n")
    
    f.write("---\n\n## Data Dictionary\n\n")
    f.writelines(all_model_tables)

# ─── 2. FEATURES CONNECTION (Rich Service Summaries) ───────────────────
with mkdocs_gen_files.open("design/features.md", "w") as f:
    f.write("# Features Connection\n\n")
    f.write("How the platform's core features connect through the service layer. Each service encapsulates business logic for a specific domain.\n\n")
    f.write(f"**Total Services Detected**: {len(all_service_summaries)}\n\n---\n\n")
    
    for svc in all_service_summaries:
        f.write(f"## {svc['name']}\n\n")
        f.write(f"**Module**: `{svc['ident']}`\n\n")
        if svc["functions"]:
            f.write("| Function | Description |\n")
            f.write("|----------|-------------|\n")
            for func in svc["functions"]:
                prefix = "🔄 " if func["is_async"] else ""
                f.write(f"| `{prefix}{func['sig']}` | {func['summary'] or '*Undocumented*'} |\n")
            f.write("\n")
        f.write(f"::: {svc['ident']}\n\n---\n\n")

# ─── 3. SYSTEM DIAGRAMS (Architecture) ─────────────────────────────────
with mkdocs_gen_files.open("design/diagrams.md", "w") as f:
    f.write("# System Diagrams\n\n")
    f.write("High-level architectural overview showing the flow from Client → API → Service → Data layers.\n")
    f.write("Connections are auto-discovered by parsing Python `import` statements.\n\n")
    f.write("```mermaid\n--8<-- \"architecture/system_diagram.mmd\"\n```\n")

# ─── 4. API ROUTES LISTING (Rich Endpoint Summaries) ───────────────────
with mkdocs_gen_files.open("design/routes.md", "w") as f:
    f.write("# API Routes Listing\n\n")
    f.write("Comprehensive list of all endpoints and their documentation, auto-detected from FastAPI routers.\n\n")
    f.write(f"**Total API Modules Detected**: {len(all_api_summaries)}\n\n---\n\n")
    
    for api in all_api_summaries:
        f.write(f"## {api['name']}\n\n")
        f.write(f"**Module**: `{api['ident']}`\n\n")
        if api["functions"]:
            f.write("| Endpoint | Description |\n")
            f.write("|----------|-------------|\n")
            for func in api["functions"]:
                prefix = "⚡ " if func["is_async"] else ""
                f.write(f"| `{prefix}{func['sig']}` | {func['summary'] or '*Undocumented*'} |\n")
            f.write("\n")
        f.write(f"::: {api['ident']}\n\n---\n\n")

# ─── SUMMARY.md ─────────────────────────────────────────────────────────
with mkdocs_gen_files.open("SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())

# Module Index fallback
with mkdocs_gen_files.open("app/index.md", "w") as f:
    f.write("# Module Index\n\nSelect a module from the sidebar to view its documentation.")
