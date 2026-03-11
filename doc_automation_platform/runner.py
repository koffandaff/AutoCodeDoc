import os
import sys
import subprocess
import time

def start_process(name, command, cwd=None):
    print(f"Starting {name}...")
    # Run the process in the background, redirecting output to the console
    process = subprocess.Popen(
        command, shell=True, cwd=cwd
    )
    return process

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    print("=== Starting AutoCodeDoc Live-Reload Servers ===")
    
    # 1. Start MkDocs serve (Usually defaults to port 8000)
    # mkdocs serve will live-reload on changes
    mkdocs_cmd = f'"{sys.executable}" -m mkdocs serve -a localhost:8000'
    p_mkdocs = start_process("MkDocs (Port 8000)", mkdocs_cmd, cwd=base_dir)

    # 2. Start Sphinx Autobuild (Defaults to port 8001)
    # sphinx-autobuild watches the source directory and rebuilds/reloads on changes
    sphinx_cmd = f'"{sys.executable}" -m sphinx_autobuild docs_sphinx site/sphinx --port 8001 --watch backend/app --watch ../docs'
    p_sphinx = start_process("Sphinx (Port 8001)", sphinx_cmd, cwd=base_dir)

    print("\n" + "="*50)
    print("Servers are running!")
    print("  - MkDocs Version: http://localhost:8000/")
    print("  - Sphinx Version: http://localhost:8001/")
    print("="*50)
    print("Press Ctrl+C to stop all servers.\n")

    try:
        # Keep the main thread alive while background processes run
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        p_mkdocs.terminate()
        p_sphinx.terminate()
        p_mkdocs.wait()
        p_sphinx.wait()
        print("Done.")

if __name__ == "__main__":
    main()
