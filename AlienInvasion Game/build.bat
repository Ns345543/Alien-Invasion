@echo off
echo Building Alien Invasion...
python build_exe.py
if %errorlevel% neq 0 (
    echo "python" command failed, trying "py"...
    py build_exe.py
)
if %errorlevel% neq 0 (
    echo Build failed. Please ensure Python is installed and in your PATH.
    pause
    exit /b
)
echo Build complete!
pause
