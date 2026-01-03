@echo off
chcp 65001 > nul
echo ============================================================
echo Test Report Viewer - Quick Start
echo ============================================================
echo.
echo Available Reports:
echo.

dir /b /ad report\easyjava_* 2>nul

if errorlevel 1 (
    echo No history reports found!
    echo Please run tests first to generate reports.
    pause
    exit /b
)

echo.
echo Options:
echo   1. View latest report (live server)
echo   2. Generate static report for sharing
echo   3. View static report with HTTP server
echo   4. List all reports
echo   5. Exit
echo.

set /p choice="Select an option (1-5): "

if "%choice%"=="1" goto view_latest
if "%choice%"=="2" goto generate_static
if "%choice%"=="3" goto view_static
if "%choice%"=="4" goto list_reports
if "%choice%"=="5" goto end
goto invalid

:view_latest
for /f "delims=" %%i in ('dir /b /ad /o-d report\easyjava_*') do (
    set latest_report=%%i
    goto found_latest
)
:found_latest
echo.
echo Opening latest report: %latest_report%
echo.
allure serve report\%latest_report%
goto end

:generate_static
echo.
set /p report_name="Enter report name (or press Enter for latest): "

if "%report_name%"=="" (
    for /f "delims=" %%i in ('dir /b /ad /o-d report\easyjava_*') do (
        set report_name=%%i
        goto generate
    )
)

:generate
echo Generating static report for: %report_name%
echo Output directory: report\static\%report_name%
if not exist "report\static\%report_name%" mkdir "report\static\%report_name%"
allure generate report\%report_name% -o report\static\%report_name% --clean
echo.
echo Static report generated successfully!
echo Location: %cd%\report\static\%report_name%
echo.
echo You can now share the 'report\static\%report_name%' folder with others.
echo Note: To view the report, use option 3 (View static report with HTTP server)
echo.
goto end

:view_static
echo.
set /p report_name="Enter report name (or press Enter for latest): "

if "%report_name%"=="" (
    for /f "delims=" %%i in ('dir /b /ad /o-d report\static\easyjava_*') do (
        set report_name=%%i
        goto serve_static
    )
)

:serve_static
echo.
echo Starting HTTP server for static report: %report_name%
echo.
python serve_report.py "report\static\%report_name%"
goto end

:list_reports
echo.
echo All Available Reports:
echo.
dir /b /ad /o-d report\easyjava_*
echo.
pause
goto end

:invalid
echo.
echo Invalid choice! Please try again.
pause
goto end

:end
