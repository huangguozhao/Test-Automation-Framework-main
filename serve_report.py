import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def start_server(directory, port=8000):
    """启动简单的HTTP服务器来查看Allure静态报告"""
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found!")
        return False
    
    abs_path = os.path.abspath(directory)
    os.chdir(abs_path)
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", port), MyHTTPRequestHandler) as httpd:
            url = f"http://localhost:{port}"
            print(f"\n{'='*60}")
            print(f"Server started successfully!")
            print(f"{'='*60}")
            print(f"Report URL: {url}")
            print(f"Report Directory: {abs_path}")
            print(f"{'='*60}")
            print(f"\nOpening browser...")
            webbrowser.open_new_tab(url)
            print(f"\nPress Ctrl+C to stop the server")
            print(f"{'='*60}\n")
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n\nServer stopped.")
                return True
                
    except OSError as e:
        if e.errno == 48 or e.errno == 10048:
            print(f"\nError: Port {port} is already in use!")
            print(f"Please try a different port or stop the other server.")
            return False
        else:
            print(f"\nError: {e}")
            return False

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter report directory path (or press Enter for latest static report): ").strip()
        
        if not directory:
            static_dir = Path('./report/static')
            if static_dir.exists():
                reports = sorted([d for d in static_dir.iterdir() if d.is_dir()], reverse=True)
                if reports:
                    directory = str(reports[0])
                    print(f"Using latest report: {directory}")
                else:
                    print("No static reports found!")
                    return
            else:
                print("No static reports found!")
                return
    
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    else:
        port_input = input("Enter port number (or press Enter for default 8000): ").strip()
        port = int(port_input) if port_input else 8000
    
    start_server(directory, port)

if __name__ == '__main__':
    main()
