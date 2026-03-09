"""Generate textual API architecture diagram dynamically."""

import os
import ast
import mkdocs_gen_files

def parse_fastapi_app(base_dir="backend/app"):
    """Scan the backend for all API, Service, Model, and Utility files."""
    components = {"api": [], "services": [], "models": [], "utils": []}
    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".py") or file == "__init__.py" or file == "main.py":
                continue
            path = os.path.join(root, file)
            module_name = file.replace(".py", "")
            if os.sep + "api" in path or "/api" in path:
                components["api"].append(module_name)
            elif os.sep + "services" in path or "/services" in path:
                components["services"].append(module_name)
            elif os.sep + "models" in path or "/models" in path:
                components["models"].append(module_name)
            elif os.sep + "utils" in path or "/utils" in path:
                components["utils"].append(module_name)
    return components

def discover_imports(base_dir="backend/app"):
    """Parse Python imports to discover real connections between layers."""
    connections = []
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".py") or file == "__init__.py":
                continue
            filepath = os.path.join(root, file)
            source_name = file.replace(".py", "")
            
            # Determine the layer prefix for this source file
            if os.sep + "api" in filepath or "/api" in filepath:
                source_prefix = "api_"
            elif os.sep + "services" in filepath or "/services" in filepath:
                source_prefix = "svc_"
            else:
                continue  # Only track API and Service connections
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())
            except:
                continue
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom) and node.module:
                    module_str = node.module
                    # API -> Service
                    if source_prefix == "api_" and "services" in module_str:
                        for alias in node.names:
                            if alias.name != "*":
                                connections.append((f"api_{source_name}", f"svc_{alias.name}", "api_to_service"))
                    # API -> Model (direct)
                    elif source_prefix == "api_" and "models" in module_str:
                        parts = module_str.split(".")
                        target = parts[-1] if len(parts) > 1 else module_str
                        connections.append((f"api_{source_name}", f"mdl_{target}", "api_to_model"))
                    # Service -> Model
                    elif source_prefix == "svc_" and "models" in module_str:
                        parts = module_str.split(".")
                        target = parts[-1] if len(parts) > 1 else module_str
                        connections.append((f"svc_{source_name}", f"mdl_{target}", "service_to_model"))

    return connections

components = parse_fastapi_app()
connections = discover_imports()

# ─── Generate Professional Mermaid Diagram with unique IDs ──────────────
mermaid = [
    "graph TD",
    '    subgraph ClientLayer ["Client Layer"]',
    '        UI["Web Interface / Mobile App"]',
    '    end',
    '',
    '    subgraph APILayer ["API Layer (Routes)"]',
    '        api_main["main.py"]'
]

for api in sorted(components["api"]):
    mermaid.append(f'        api_{api}["{api}.py"]')
mermaid.append("    end")
mermaid.append("")

mermaid.append('    subgraph ServiceLayer ["Service Layer (Business Logic)"]')
for service in sorted(components["services"]):
    mermaid.append(f'        svc_{service}["{service}.py"]')
mermaid.append("    end")
mermaid.append("")

mermaid.append('    subgraph DataLayer ["Data Layer (Models)"]')
for model in sorted(components["models"]):
    mermaid.append(f'        mdl_{model}["{model}.py"]')
mermaid.append("    end")
mermaid.append("")

if components["utils"]:
    mermaid.append('    subgraph UtilsLayer ["Utilities"]')
    for util in sorted(components["utils"]):
        mermaid.append(f'        utl_{util}["{util}.py"]')
    mermaid.append("    end")
    mermaid.append("")

# Connect Client -> Main -> All API routes
mermaid.append("    UI --> api_main")
for api in sorted(components["api"]):
    mermaid.append(f"    api_main --> api_{api}")

# Connect using REAL import analysis (with prefixed IDs)
connected_pairs = set()
for source, target, conn_type in connections:
    pair = (source, target)
    if pair not in connected_pairs:
        connected_pairs.add(pair)
        mermaid.append(f"    {source} --> {target}")

# Write Mermaid to virtual file
with mkdocs_gen_files.open("architecture/system_diagram.mmd", "w") as f:
    f.write("\n".join(mermaid))

# Keep the original tree as well
content = ["FastAPI Application Architecture Tree", "=====================================\n", "├── API Routes"]
for api in sorted(components["api"]):
    content.append(f"│    ├── {api}")
content.append("│\n├── Service Layer")
for service in sorted(components["services"]):
    content.append(f"│    ├── {service}")
content.append("│\n├── Data Models")
for model in sorted(components["models"]):
    content.append(f"     ├── {model}")
if components["utils"]:
    content.append("│\n├── Utilities")
    for util in sorted(components["utils"]):
        content.append(f"     ├── {util}")

with mkdocs_gen_files.open("architecture/system_architecture.txt", "w") as f:
    f.write("\n".join(content))
