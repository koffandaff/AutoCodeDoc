# 🚀 Documentation Automation & Verification

This guide explains how to ensure your documentation stays in sync with your code and how to verify it.

## 🔄 Automatic Updates
The documentation is configured to **automatically update** every time you build or serve the site. This is handled by the `gen-files` plugin in `mkdocs.yml`, which triggers:
- `scripts/gen_ref_pages.py`: Generates the Python API reference.
- `scripts/gen_architecture.py`: Updates the system architecture tree.

### The "One Command" to Rule Them All
Run this from the project root (`doc_automation_platform`) to start a live-reloading server:

```bash
python scripts/run_pipeline.py
```

> [!TIP]
> **Live Updates**: While the server is running, any changes you make to `.py` files in `backend/app/` or `.md` files in `docs/` will be reflected immediately in the browser.

## 🚀 Unified Pipeline (CI/CD Ready)
The easiest way to check everything is to run the master pipeline script. This is what you would use in GitHub Actions:

```bash
# Run integrity checks + build + serve
.\venv\Scripts\python.exe scripts/run_pipeline.py --serve

# Build only (for CI/CD)
.\venv\Scripts/python.exe scripts/run_pipeline.py --build-only
```

## 🧪 Verification Checklist

1.  **Start the server** using the command above.
2.  **Open** [http://127.0.0.1:8001/AutoCodeDoc/](http://127.0.0.1:8001/AutoCodeDoc/) in your browser.
3.  **Check System Design**: Click **Design > Overview** to see the architecture tree.
4.  **Check API Docs**: Click **API Reference > API > app > api > auth** to verify the code reference.
5.  **Verify No 404s**: Every link in the sidebar should now resolve correctly.
6.  **Documentation Integrity**
    - Run `.\venv\Scripts\python.exe scripts/check_doc_sync.py`
    - Verify it returns "All fields are correctly documented!"

## 🛠️ Troubleshooting
If you don't see your changes:
- Check the terminal for any Python errors in the generation scripts.
- Ensure you have saved your code changes.
- Restart the `mkdocs serve` command.
