.. AutoCodeDoc Platform documentation master file

============================================
AutoCodeDoc Platform — Documentation Hub
============================================

.. image:: https://img.shields.io/badge/docs-Sphinx-blue?style=for-the-badge&logo=sphinx
   :alt: Sphinx Docs
.. image:: https://img.shields.io/badge/API-AutoAPI-green?style=for-the-badge
   :alt: AutoAPI
.. image:: https://img.shields.io/badge/coverage-interrogate-orange?style=for-the-badge
   :alt: Interrogate
.. image:: https://img.shields.io/badge/diagrams-Mermaid.js-purple?style=for-the-badge
   :alt: Mermaid

**A production-grade, automated documentation engine** that turns your Python code into
a beautiful, live-updating documentation site — powered entirely by NumPy-style docstrings.

.. grid:: 2

   .. grid-item-card:: Getting Started
      :link: guides/installation
      :link-type: doc

      Install dependencies, set up your environment, and start building.

   .. grid-item-card:: API Reference
      :link: api/index
      :link-type: doc

      Auto-generated from source code — every module, class, and function.

   .. grid-item-card:: Architecture
      :link: architecture/system_diagram
      :link-type: doc

      System diagrams, ER models, and cross-repo data flow — all auto-generated.


Quick Links
-----------

- **Home**: `Documentation Hub <index.html>`_
- **Live MkDocs Site**: `Legacy MkDocs Documentation </AutoCodeDoc/legacy-docs/>`_
- **GitHub Repository**: `koffandaff/AutoCodeDoc <https://github.com/koffandaff/AutoCodeDoc>`_
- **FastAPI OpenAPI Docs**: Available at ``/docs`` when the server is running

Key Features
------------

- **Zero-Maintenance API Docs** — ``sphinx-autoapi`` recursively scans the codebase
- **AST-Based Diagrams** — System architecture, ER diagrams, and data flow graphs auto-generated from code
- **Cross-Repo Awareness** — Documents interactions between services
- **Docstring Coverage** — ``interrogate`` integration with non-blocking CI alerts
- **NumPy-Style Docstrings** — Full parameter, return, and exception documentation throughout
- **Single-Command Build** — ``python run_pipeline.py`` builds everything end-to-end


.. toctree::
   :maxdepth: 2
   :caption: Guides

   guides/installation
   guides/usage
   guides/contributing
   changelog

.. toctree::
   :maxdepth: 3
   :caption: API Reference

   api/index

.. toctree::
   :maxdepth: 2
   :caption: Architecture

   architecture/system_diagram
   architecture/er_diagram
   architecture/cross_repo_flow

.. toctree::
   :maxdepth: 1
   :caption: External

   MkDocs Site <https://koffandaff.github.io/AutoCodeDoc/legacy-docs/>


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
