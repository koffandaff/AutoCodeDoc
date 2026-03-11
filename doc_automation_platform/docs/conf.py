"""
Sphinx Configuration for AutoCodeDoc Platform
==============================================

Primary documentation engine using sphinx-autoapi for fully automated
API reference generation from NumPy-style docstrings.
"""

import os
import sys
from datetime import datetime

# ─── Path Setup ──────────────────────────────────────────────────────────
# Add backend to sys.path so autoapi can discover all modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

# ─── Project Metadata ───────────────────────────────────────────────────
project = 'AutoCodeDoc Platform'
copyright = f'{datetime.now().year}, AutoCodeDoc Team'
author = 'AutoCodeDoc Team'
version = '1.0'
release = '1.0.0'

# ─── Extensions ──────────────────────────────────────────────────────────
extensions = [
    # Core Sphinx
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',

    # AutoAPI — fully automated, no manual .. automodule:: needed
    'autoapi.extension',

    # Napoleon — NumPy-style docstring support
    'sphinx.ext.napoleon',

    # Type hints in signatures
    'sphinx_autodoc_typehints',

    # Markdown support via MyST
    'myst_parser',

    # Mermaid.js diagrams
    'sphinxcontrib.mermaid',

    # UI components (cards, tabs, grids)
    'sphinx_design',

    # Copy button on code blocks
    'sphinx_copybutton',
]

# ─── AutoAPI Configuration ───────────────────────────────────────────────
# Recursively scan the backend codebase — fully hands-off
autoapi_type = 'python'
autoapi_dirs = [os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app'))]
autoapi_root = 'api'
autoapi_ignore = ['*/__pycache__/*', '*/migrations/*', '*_test.py', '*tests*']
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'imported-members',
    'special-members',
]
autoapi_python_class_content = 'both'  # Show both class docstring and __init__
autoapi_member_order = 'groupwise'
autoapi_keep_files = True  # Keep generated .rst files for debugging
autoapi_add_toctree_entry = False

# ─── Napoleon Configuration (NumPy-style) ────────────────────────────────
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_attr_annotations = True

# ─── MyST Parser Configuration ──────────────────────────────────────────
myst_enable_extensions = [
    'colon_fence',       # ::: directive syntax
    'deflist',           # Definition lists
    'fieldlist',         # Field lists
    'html_admonition',   # HTML admonitions
    'html_image',        # HTML images
    'substitution',      # Substitution references
    'tasklist',          # Task lists with checkboxes
]
myst_heading_anchors = 3
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# ─── Intersphinx — Cross-Repo Links ─────────────────────────────────────
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pydantic': ('https://docs.pydantic.dev/latest/', None),
    'fastapi': ('https://fastapi.tiangolo.com/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'torch': ('https://pytorch.org/docs/stable/', None),
}

# ─── Mermaid Configuration ───────────────────────────────────────────────
mermaid_version = '10.6.1'
mermaid_init_js = """
mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
        primaryColor: '#4051b5',
        primaryTextColor: '#ffffff',
        primaryBorderColor: '#303f9f',
        lineColor: '#5c6bc0',
        secondaryColor: '#e8eaf6',
        tertiaryColor: '#f5f5f5',
        fontSize: '14px'
    },
    flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
    },
    er: {
        useMaxWidth: true,
        fontSize: 12
    }
});
"""

# ─── HTML Output Configuration ───────────────────────────────────────────
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_static_path = ['_static']
html_css_files = ['custom.css']
html_title = 'AutoCodeDoc Platform'
html_short_title = 'AutoCodeDoc'
html_show_sourcelink = True
html_show_copyright = True

# Persistent MkDocs link in navbar — injected via template
html_context = {
    'mkdocs_url': '/AutoCodeDoc/legacy-docs/',
    'display_github': True,
    'github_user': 'koffandaff',
    'github_repo': 'AutoCodeDoc',
    'github_version': 'main',
    'conf_py_path': '/doc_automation_platform/docs/',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/__pycache__', 'index.md']
suppress_warnings = ['toc.not_included']

# ─── Autodoc defaults ───────────────────────────────────────────────────
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
}

# ─── Todo Configuration ─────────────────────────────────────────────────
todo_include_todos = True

# ─── Graphviz Configuration ─────────────────────────────────────────────
graphviz_output_format = 'svg'
