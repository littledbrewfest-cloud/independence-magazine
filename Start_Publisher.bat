@echo off
title Independence Magazine - Editorial Studio (WordPress CMS)
color 0F
cls
echo =====================================================================
echo       INDEPENDENCE MAGAZINE -- WORDPRESS-STYLE EDITORIAL STUDIO
echo =====================================================================
echo.
echo Starting local editorial server...
cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] Python detected. Launching Editorial Studio...
    python admin_publisher.py
    goto end
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] Py launcher detected. Launching Editorial Studio...
    py admin_publisher.py
    goto end
)

echo [ERROR] Python was not found in your system PATH.
echo Please ensure Python is installed and added to PATH.
pause

:end
