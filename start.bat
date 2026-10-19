@echo off
cd /d "%~dp0"
py server.py --open %*
if errorlevel 9009 python server.py --open %*
pause
