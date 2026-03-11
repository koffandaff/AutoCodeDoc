#!/bin/bash
echo "Building MkDocs..."
venv/bin/mkdocs build -d site

echo ""
echo "Building Sphinx Docs..."
venv/bin/sphinx-build -b html docs_sphinx site/sphinx

echo ""
echo "Done! You can now serve the combined documentation:"
echo "python -m http.server 8000 -d site"
