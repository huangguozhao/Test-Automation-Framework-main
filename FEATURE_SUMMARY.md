# Test History Reports Feature

## Overview
This feature enables automatic preservation of test history reports with timestamp-based directory naming. Each test run generates a unique report directory, allowing you to track and compare test results over time.

## What's New

### 1. Automatic History Preservation
- Every test run creates a new report directory with timestamp
- No more overwriting previous reports
- Easy comparison between different test runs

### 2. Report Naming Convention
Format: `easyjava_YYYYMMDD_HHMMSS`

Examples:
- `easyjava_20260103_080007` - Generated on 2026-01-03 at 08:00:07
- `easyjava_20260103_080202` - Generated on 2026-01-03 at 08:02:02

### 3. Report Viewer Tools
Two convenient tools for viewing and sharing reports:

#### view_report.bat (Windows)
- Quick start batch script
- Easy-to-use menu interface
- Best for Windows users

#### view_report.py (Python)
- Cross-platform compatible
- More features and options
- Best for advanced users

## How to Use

### Running Tests
Run tests as usual:
```bash
python run.py
```

A new report directory will be created automatically.

### Viewing Reports

#### Option 1: Using Batch Script (Windows)
```bash
view_report.bat
```

#### Option 2: Using Python Script
```bash
python view_report.py
```

### Sharing Reports

1. Generate a static report:
   ```bash
   view_report.bat
   # Select option 2
   # Choose the report to share
   ```

2. Share the generated folder:
   - Location: `./report/static/{report_name}/`
   - Share the entire folder with others
   - Recipients open `index.html` to view

## Directory Structure

```
report/
├── easyjava_20260103_080007/      # First test run
│   ├── *.json                     # Test result files
│   ├── *.txt                      # Attachment files
│   ├── container.json             # Test containers
│   └── environment.xml            # Environment info
├── easyjava_20260103_080202/      # Second test run
│   └── ...                        # Same structure
├── static/                        # Generated HTML reports
│   └── easyjava_20260103_080007/
│       ├── index.html             # Main report page
│       ├── styles.css             # Styles
│       ├── app.js                 # JavaScript
│       └── data/                  # Report data
└── results.xml                    # JUnit XML results
```

## Changes Made

### Modified Files
1. **run.py**
   - Added timestamp generation
   - Changed report directory to use timestamp
   - Removed `--clean-alluredir` parameter
   - Support for both Allure and TM reports

2. **pytest.ini**
   - Removed `--clean-alluredir` parameter

3. **conftest.py**
   - Removed report file deletion logic
   - Kept YAML data cleanup

### New Files
1. **view_report.py** - Python script for viewing and generating reports
2. **view_report.bat** - Windows batch script for quick access
3. **REPORT_VIEWER_GUIDE.md** - English documentation
4. **报告查看器使用指南.md** - Chinese documentation
5. **FEATURE_SUMMARY.md** - This file

## Features

### ✅ Automatic History Preservation
- Every test run creates a unique report directory
- No manual configuration needed
- Timestamp-based naming for easy identification

### ✅ Easy Report Viewing
- Interactive live server for local viewing
- Static HTML generation for sharing
- Menu-driven interface

### ✅ Report Sharing
- Generate portable HTML reports
- Share with team members or stakeholders
- No server required for viewing shared reports

### ✅ Backward Compatible
- Works with existing test framework
- No changes to test execution
- Allure and TM report formats supported

## Benefits

1. **Historical Tracking**: Compare test results over time
2. **Trend Analysis**: Identify patterns and regressions
3. **Audit Trail**: Keep records of all test executions
4. **Easy Sharing**: Share reports with anyone, anytime
5. **No Data Loss**: All reports are preserved automatically

## Troubleshooting

### Issue: Reports not being preserved
**Solution**: Check that you're using the updated `run.py` file

### Issue: Allure command not found
**Solution**: Install Allure and add to PATH
- Download: https://docs.qameta.io/allure/
- Verify: `allure --version`

### Issue: Report viewer not working
**Solution**: Ensure Python 3.6+ and Allure are installed

## Requirements

- Python 3.6+
- Allure Command-line (for Allure reports)
- Modern web browser

## Documentation

- **English**: See `REPORT_VIEWER_GUIDE.md`
- **Chinese**: See `报告查看器使用指南.md`
- **Allure Docs**: https://docs.qameta.io/allure/

## Git Information

- **Branch**: `feature/preserve-history-reports`
- **Commit**: `9a58471`
- **Files Changed**: 3 modified, 5 new

## Support

For issues or questions:
1. Check the documentation files
2. Review the example usage
3. Verify Allure installation
4. Check Python version compatibility
