import subprocess
import sys
import os
import argparse

def run_step(name, command, cwd="."):
    """Execute a shell command as a pipeline step."""
    print(f"\n🚀 STEP: {name}")
    print(f"Executing: {command}")
    
    result = subprocess.run(command, shell=True, cwd=cwd)
    
    if result.returncode != 0:
        print(f"\n❌ FAILED: {name} exited with code {result.returncode}")
        return False
    
    print(f"✅ SUCCESS: {name} completed.")
    return True

def main():
    parser = argparse.ArgumentParser(description="AutoCodeDoc CI/CD Pipeline Orchestrator")
    parser.add_argument("--build-only", action="store_true", help="Run checks and build without serving")
    parser.add_argument("--serve", action="store_true", default=True, help="Start the live server (default)")
    args = parser.parse_args()

    # If build-only is requested, override serve
    if args.build_only:
        args.serve = False

    # Smart Venv Detection
    venv_python = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")
    if os.path.exists(venv_python):
        python_exe = venv_python
        print(f"📌 Using local venv: {python_exe}")
    else:
        python_exe = sys.executable
        print(f"⚠️  Venv not found at {venv_python}. Using: {python_exe}")

    # Step 1: Documentation Integrity Check
    if not run_step("Doc Integrity Check", f"{python_exe} scripts/check_doc_sync.py"):
        sys.exit(1)

    # Step 2: Architecture Tree Generation
    if not run_step("Architecture Generation", f"{python_exe} scripts/gen_architecture.py"):
        sys.exit(1)

    # Step 3: API Reference & Design Doc Generation
    if not run_step("API & Design Generation", f"{python_exe} scripts/gen_ref_pages.py"):
        sys.exit(1)

    # Step 4: MkDocs Build (Verification)
    if not run_step("MkDocs Build Verification", f"{python_exe} -m mkdocs build --no-directory-urls"):
        sys.exit(1)

    print("\n🎉 PIPELINE COMPLETE: Your documentation is healthy and built successfully!")

    # Step 5: Optional Serve
    if args.serve:
        print("\n🌐 Starting Live Server at http://127.0.0.1:8001")
        run_step("MkDocs Serve", f"{python_exe} -m mkdocs serve --no-directory-urls -a 127.0.0.1:8001")

if __name__ == "__main__":
    main()
