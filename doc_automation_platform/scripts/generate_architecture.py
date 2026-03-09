import os

def parse_fastapi_app(base_dir="backend/app"):
    """
    Parses the FastAPI backend directory to find routers, services, and models.
    Returns a dictionary of found components.
    """
    components = {
        "api": [],
        "services": [],
        "models": []
    }
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".py") or file == "__init__.py":
                continue
                
            path = os.path.join(root, file)
            module_name = file.replace(".py", "")
            
            if "api" in path:
                components["api"].append(module_name)
            elif "services" in path:
                components["services"].append(module_name)
            elif "models" in path:
                components["models"].append(module_name)
                
    return components

def generate_text_diagram(output_path="docs/architecture/system_architecture.txt"):
    """
    Generates a text-based architecture tree since Graphviz is not installed globally.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    components = parse_fastapi_app()
    
    content = [
        "FastAPI Application Architecture Tree",
        "=====================================\n",
        "├── API Routes"
    ]
    
    for api in components["api"]:
        content.append(f"│    ├── {api}")
        
    content.append("│")
    content.append("├── Service Layer")
    for service in components["services"]:
        content.append(f"│    ├── {service}")
        
    content.append("│")
    content.append("└── Data Models")
    for model in components["models"]:
        content.append(f"     ├── {model}")
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

if __name__ == "__main__":
    print("Generating textual architecture diagram fallback...")
    generate_text_diagram()
    print("Diagram successfully generated at docs/architecture/system_architecture.txt")
