import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def list_reports():
    """列出所有可用的历史报告"""
    report_dir = Path('./report')
    if not report_dir.exists():
        print("Report directory not found!")
        return []
    
    reports = []
    for item in report_dir.iterdir():
        if item.is_dir() and item.name.startswith('easyjava_'):
            reports.append(item.name)
    
    return sorted(reports, reverse=True)

def view_report(report_name=None):
    """查看指定的历史报告"""
    reports = list_reports()
    
    if not reports:
        print("No history reports found!")
        return
    
    if report_name is None:
        print("\nAvailable reports:")
        for i, report in enumerate(reports, 1):
            print(f"  {i}. {report}")
        
        try:
            choice = int(input("\nSelect a report number to view (or 0 to exit): "))
            if choice == 0:
                return
            if 1 <= choice <= len(reports):
                report_name = reports[choice - 1]
            else:
                print("Invalid choice!")
                return
        except ValueError:
            print("Invalid input!")
            return
    elif report_name not in reports:
        print(f"Report '{report_name}' not found!")
        return
    
    report_path = Path(f'./report/{report_name}')
    print(f"\nOpening report: {report_name}")
    print(f"Report path: {report_path.absolute()}")
    
    try:
        subprocess.run(f'allure serve {report_path}', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open report: {e}")
        print("Make sure allure is installed and available in PATH")

def generate_static_report(report_name=None, output_dir=None):
    """生成静态HTML报告，方便分享"""
    reports = list_reports()
    
    if not reports:
        print("No history reports found!")
        return
    
    if report_name is None:
        print("\nAvailable reports:")
        for i, report in enumerate(reports, 1):
            print(f"  {i}. {report}")
        
        try:
            choice = int(input("\nSelect a report number to generate (or 0 to exit): "))
            if choice == 0:
                return
            if 1 <= choice <= len(reports):
                report_name = reports[choice - 1]
            else:
                print("Invalid choice!")
                return
        except ValueError:
            print("Invalid input!")
            return
    elif report_name not in reports:
        print(f"Report '{report_name}' not found!")
        return
    
    report_path = Path(f'./report/{report_name}')
    
    if output_dir is None:
        output_dir = Path(f'./report/static/{report_name}')
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nGenerating static report...")
    print(f"Source: {report_path.absolute()}")
    print(f"Output: {output_dir.absolute()}")
    
    try:
        subprocess.run(f'allure generate {report_path} -o {output_dir} --clean', shell=True, check=True)
        print(f"\nStatic report generated successfully!")
        print(f"Report location: {output_dir.absolute()}")
        print(f"\nYou can share the '{output_dir}' folder with others.")
        print(f"Open 'index.html' in the folder to view the report.")
        
        open_report = input("\nOpen the report now? (y/n): ").lower()
        if open_report == 'y':
            index_file = output_dir / 'index.html'
            webbrowser.open_new_tab(str(index_file.absolute()))
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate report: {e}")
        print("Make sure allure is installed and available in PATH")

def main():
    print("=" * 60)
    print("Test Report Viewer")
    print("=" * 60)
    
    while True:
        print("\nOptions:")
        print("  1. List all history reports")
        print("  2. View a report (live server)")
        print("  3. Generate static report for sharing")
        print("  4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            reports = list_reports()
            if reports:
                print("\nAvailable reports:")
                for report in reports:
                    print(f"  - {report}")
            else:
                print("No history reports found!")
        
        elif choice == '2':
            report_name = input("\nEnter report name (or leave empty to select from list): ").strip()
            if report_name:
                view_report(report_name)
            else:
                view_report()
        
        elif choice == '3':
            report_name = input("\nEnter report name (or leave empty to select from list): ").strip()
            output_dir = input("Enter output directory (or leave empty for default): ").strip()
            if report_name:
                if output_dir:
                    generate_static_report(report_name, output_dir)
                else:
                    generate_static_report(report_name)
            else:
                if output_dir:
                    generate_static_report(output_dir=output_dir)
                else:
                    generate_static_report()
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
