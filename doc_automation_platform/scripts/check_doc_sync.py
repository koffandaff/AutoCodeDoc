import os
import sys
import inspect
from pydantic import BaseModel

# Add backend to path so we can import app
sys.path.append(os.path.join(os.getcwd(), 'backend'))

def check_model_docs(module_name: str):
    """Validate that all Pydantic fields in a module have descriptions."""
    try:
        module = __import__(module_name, fromlist=['*'])
    except ImportError as e:
        print(f"Error: Could not import {module_name}: {e}")
        return False

    errors = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj != BaseModel:
            print(f"Checking class: {name}")
            for field_name, field in obj.model_fields.items():
                if not field.description:
                    errors.append(f"❌ MISSED FIELD: '{field_name}' in class '{name}' is missing a description!")
                else:
                    print(f"  ✅ {field_name}: {field.description}")

    if errors:
        print("\n--- Documentation Integrity Errors ---")
        for err in errors:
            print(err)
        return False
    
    print("\n✅ All fields are correctly documented!")
    return True

def check_all_models():
    """Verify documentation for all models deeply nested in the app.models package."""
    from pathlib import Path
    models_dir = Path(os.getcwd()) / 'backend' / 'app' / 'models'
    overall_success = True
    
    for path in models_dir.rglob("*.py"):
        if path.name == '__init__.py':
            continue
            
        # Convert path to module name: e.g., app.models.ecommerce.billing.invoice
        # Get relative path from backend/app/models
        rel_parts = path.relative_to(models_dir.parent.parent).with_suffix('').parts
        module_name = ".".join(rel_parts)
        
        if not check_model_docs(module_name):
            overall_success = False
            
    return overall_success

if __name__ == "__main__":
    if not check_all_models():
        sys.exit(1)
