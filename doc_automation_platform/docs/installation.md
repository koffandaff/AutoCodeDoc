# Installation Guide

Welcome to the installation documentation. You can run this platform in multiple environments.

## Local Environment (Direct)

To install this documentation automation platform locally on Windows:

1. Clone the repository:
   ```bash
   git clone https://github.com/example/doc_automation_platform.git
   ```
2. Set up the Python Virtual Environment:
   ```bash
   cd doc_automation_platform/backend
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the documentation server:
   ```bash
   python scripts/run_pipeline.py
   ```
5. View the docs at: **[http://127.0.0.1:8001/AutoCodeDoc/](http://127.0.0.1:8001/AutoCodeDoc/)**

## Production Environment

We currently advise using Docker to serve the MkDocs site in a containerized format, which we will document in a future sprint.
