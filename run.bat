@echo off
title AegisBridge
color 0A
echo.
echo  ================================================
echo   AEGISBRIDGE  -  AI Bridge Health Monitor
echo  ================================================
echo.

where py >nul 2>&1
if %errorlevel%==0 (
    echo  [OK] Python found  ^(py^)
    echo  [OK] Starting server...
    echo.
    echo  Opening http://localhost:5000
    echo  Keep this window open!
    echo  Press Ctrl+C to stop.
    echo.
    py server.py
    goto :done
)

where python >nul 2>&1
if %errorlevel%==0 (
    echo  [OK] Python found  ^(python^)
    echo  [OK] Starting server...
    echo.
    echo  Opening http://localhost:5000
    echo  Keep this window open!
    echo  Press Ctrl+C to stop.
    echo.
    python server.py
    goto :done
)

where python3 >nul 2>&1
if %errorlevel%==0 (
    echo  [OK] Python found  ^(python3^)
    echo  [OK] Starting server...
    echo.
    python3 server.py
    goto :done
)

echo  [ERROR] Python not found!
echo.
echo  Download Python from: https://www.python.org/downloads/
echo  Tick "Add Python to PATH" during install.
echo.

:done
echo.
echo  Server stopped. Press any key to close.
pause >nul
