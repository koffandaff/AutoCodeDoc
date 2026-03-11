@echo off
echo ======================================================
echo    AutoCodeDoc: Automated Live Documentation
echo ======================================================
echo.

:: Detect if we are in the right directory
if not exist "run_pipeline.py" (
    echo [ERROR] Please run this script from the project root.
    pause
    exit /b 1
)

:: Check if venv exists, if so activate it
if exist "venv\Scripts\activate.bat" (
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate.bat
)

:: Install requirements if needed (optional, could be slow)
:: echo [INFO] Ensuring dependencies are up-to-date...
:: pip install -r requirements.txt

echo [INFO] Starting automatic documentation watcher...
echo [HINT] This will refresh your browser automatically on every code change.
echo [HINT] Press Ctrl+C to stop.
echo.

python scripts\watch_docs.py

pause
