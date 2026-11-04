@echo off
rem One command to set up the Python that the "AI engineer" courses use: %USERPROFILE%\.codequest\ai-venv
cd /d "%~dp0"
set "TARGET=%USERPROFILE%\.codequest\ai-venv"
py -3.12 -m venv "%TARGET%" || (echo Python 3.12 from python.org is needed: https://www.python.org/downloads/ & pause & exit /b 1)
"%TARGET%\Scripts\python" -m pip install --upgrade pip || goto :fail
"%TARGET%\Scripts\python" -m pip install torch || goto :fail
"%TARGET%\Scripts\python" -m pip install -r requirements-ai.txt || goto :fail
"%TARGET%\Scripts\python" -c "import numpy, pandas, torch, sklearn, fastapi; print('All AI packages work. Press Run in AI engineer 1, lesson 01.')" || goto :fail
pause
exit /b 0
:fail
echo Something went wrong above. Copy the red text into the lesson's hint or ask Claude.
pause
exit /b 1
