@echo off
:ulang
python rmon_tool.py

echo.
set /p ulangi=Jalankan lagi? [Y/N]:
if /I "%ulangi%"=="Y" goto ulang
