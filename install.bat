@echo off
setlocal
title Install CodeQuest
cd /d "%~dp0"

rem Find Python 3.9 or newer. "py" is the Python launcher from python.org.
rem The Microsoft Store Python is skipped: it redirects AppData writes, which breaks the shortcuts.
set "PY="
py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) and 'WindowsApps' not in sys.executable else 1)" >nul 2>&1 && set "PY=py -3"
if not defined PY (
    python -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) and 'WindowsApps' not in sys.executable else 1)" >nul 2>&1 && set "PY=python"
)
if defined PY goto install

echo CodeQuest needs Python 3.9 or newer from python.org.
echo (The Microsoft Store version of Python doesn't work for this.)
echo.
where winget >nul 2>&1
if errorlevel 1 goto manual
choice /m "Install Python now"
if errorlevel 2 goto manual
winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
echo.
echo Python is installed. Close this window and double-click install.bat again.
pause
exit /b 0

:manual
echo Download Python from https://www.python.org/downloads/
echo While installing, tick "Add python.exe to PATH". Then double-click install.bat again.
pause
exit /b 1

:install
%PY% install_windows.py %*
pause
