@echo off
echo ======================================================
echo    AutoCodeDoc: Full Documentation Pipeline
echo ======================================================
echo.

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

echo [INFO] Running full build pipeline...
echo (Includes: Lint, Coverage, Diagrams, Sphinx, MkDocs)
echo.

python run_pipeline.py --build-only

echo.
echo ======================================================
echo BUILD COMPLETE
echo Check docs_report.json for details.
echo Output: site\sphinx\index.html
echo ======================================================
pause
