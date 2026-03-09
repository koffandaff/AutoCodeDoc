# AutoCodeDoc Platform (automated Docs at: https://koffandaff.github.io/AutoCodeDoc/)

A production-grade, automated documentation engine that turns your Python code into a beautiful, live-updating documentation site.

## Features

- **Automated API Reference**: Every FastAPI route is documented instantly with technical parameters, response types, and raises.
- **Dynamic Architecture Diagrams**: A custom AST (Abstract Syntax Tree) parser scans your Python imports to generate a real-time graph of how your API, Services, and Models connect.
- **Dynamic ER Diagrams**: True Entity-Relationship diagrams generated directly from your Pydantic models, including field-level attributes (Int, Str, etc.).
- **Doc Integrity Checker**: A recursive guardrail (`check_doc_sync.py`) that ensures all Pydantic fields have descriptions before allowing a build.
- **Single-Command Pipeline**: Run `python scripts/run_pipeline.py` to check integrity, generate diagrams, and serve/build the site in one go.

---

## Outputs: 

1. ### DocFormat:
   <img width="1686" height="975" alt="image" src="https://github.com/user-attachments/assets/8721cbed-db87-47d3-a41a-d5e4bf46c439" />

2. ### CI/CD Pipeline Testcase
   
   * ### Case1: (Error in auto document as no proper comment strucutre)
     
      <img width="903" height="303" alt="image" src="https://github.com/user-attachments/assets/eabf637c-8c00-4748-ad5f-d5e66a72248d" />
      <img width="1439" height="266" alt="image" src="https://github.com/user-attachments/assets/51e0a3f8-a5cf-4767-a54b-673a2ee76d58" />
      
   * ### Case2 : (Structured Code)
     
      <img width="1011" height="488" alt="image" src="https://github.com/user-attachments/assets/e513feb6-0dbe-49cf-9cd5-2b7d090fef20" />
      <img width="1424" height="379" alt="image" src="https://github.com/user-attachments/assets/826a7394-d9c3-4263-9804-79d0c6fbccfe" />
      (Pages built right after the code is pushed and there's a change in backend file in that commit)
     
4. ### Results:
   
   * ### Before Case2 commit:
     
        <img width="1874" height="926" alt="image" src="https://github.com/user-attachments/assets/59836f20-5275-4702-bb6e-7da950ed1dc7" />
        
   * ### After Case2 Push(notification docs is added in Api documentation and others as well):
   * 
        <img width="1827" height="961" alt="560569375-fbce20c6-685e-42fd-925f-76c90c28a419" src="https://github.com/user-attachments/assets/fbd985a9-a438-4757-b460-7b9825b04d65" />




---
## Tech Stack

- **Core**: Python 3.x, FastAPI, Pydantic v2
- **Documentation**: [MkDocs](https://www.mkdocs.org/) with [Material Theme](https://squidfunk.github.io/mkdocs-material/)
- **Automation**: `mkdocstrings`, `mkdocs-gen-files`, `mkdocs-literate-nav`, `mkdocs-section-index`
- **Diagrams**: [Mermaid.js](https://mermaid.js.org/) injected via AST parsing
- **CI/CD**: GitHub Actions
- **Hosting**: GitHub Pages

## Project Structure

```text
├── .github/workflows/      # CI/CD Automation
├── backend/
│   └── app/                # Main Application Logic
│       ├── api/            # FastAPI Endpoints
│       ├── models/         # Pydantic Schemas (Data Layer)
│       └── services/       # Business Logic Layer
├── docs/                   # Static Markdown Documentation
├── scripts/                # The Automation Engine
│   ├── gen_ref_pages.py    # Generates the API Reference
│   ├── gen_architecture.py # AST-based architecture generator
│   ├── check_doc_sync.py   # Documentation integrity guard
│   └── run_pipeline.py     # Pipeline orchestrator
├── mkdocs.yml              # Documentation Configuration
└── requirements.txt        # Documentation Dependencies
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Pipeline**:
   ```bash
   python scripts/run_pipeline.py
   ```
3. **View the Site**: Open [http://127.0.0.1:8001/AutoCodeDoc/](http://127.0.0.1:8001/AutoCodeDoc/) in your browser.

## CI/CD & Hosting

This project is pre-configured to host on **GitHub Pages**.

- **Workflow**: Every push to `main` triggers an automated integrity check. If it passes, the site is built and deployed to your GitHub repository's `gh-pages` branch.
- **Live URL**: `https://koffandaff.github.io/AutoCodeDoc/`

---

*Built with ❤️ for automated, developer-first documentation.*
