#!/usr/bin/env python3
"""
新系统测试运行脚本
自动启动测试并生成Allure报告
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path
import requests
import shutil

def check_dependencies():
    """检查必要的依赖"""
    print("🔍 检查依赖...")
    
    # 检查pytest
    try:
        import pytest
        print("✅ pytest 已安装")
    except ImportError:
        print("❌ pytest 未安装，请运行: pip install pytest")
        return False
    
    # 检查allure
    try:
        result = subprocess.run(["allure", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ allure 已安装")
        else:
            print("❌ allure 未安装，请安装 Allure")
            return False
    except FileNotFoundError:
        print("❌ allure 未安装，请安装 Allure")
        return False
    
    return True

def check_mock_server():
    """检查Mock服务器状态"""
    print("📡 检查Mock服务器状态...")
    
    try:
        # 尝试访问登录接口
        response = requests.post(
            "http://127.0.0.1:8787/dar/user/login",
            data={"user_name": "test01", "passwd": "admin123"},
            timeout=3
        )
        if response.status_code == 200:
            print("✅ Mock服务器运行正常")
            return True
        else:
            print(f"⚠️ Mock服务器响应异常: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Mock服务器未启动或无法访问: {e}")
        print("请先启动Mock服务器:")
        print("  cd mock_server/api_server")
        print("  python base/flask_service.py")
        return False

def clean_old_reports():
    """清理旧的测试报告"""
    print("🧹 清理旧报告...")
    
    report_dirs = [
        "report/new_system_temp",
        "report/new_system_html"
    ]
    
    for report_dir in report_dirs:
        path = Path(report_dir)
        if path.exists():
            shutil.rmtree(path)
            print(f"  删除: {report_dir}")

def run_tests():
    """运行新系统测试"""
    print("🧪 运行新系统测试...")
    
    # 确保报告目录存在
    Path("report").mkdir(exist_ok=True)
    
    # 构建测试命令
    cmd = [
        "pytest",
        "example_new_system/testcase/",
        "--alluredir=report/new_system_temp",
        "-v",
        "--tb=short",
        "--strict-markers"
    ]
    
    print(f"执行命令: {' '.join(cmd)}")
    
    # 运行测试
    result = subprocess.run(cmd, text=True)
    
    return result.returncode == 0

def generate_allure_report():
    """生成并打开Allure报告"""
    print("📈 生成Allure报告...")
    
    report_temp = Path("report/new_system_temp")
    if not report_temp.exists():
        print("❌ 测试数据目录不存在，请先运行测试")
        return False
    
    try:
        # 尝试启动Allure服务
        print("启动Allure服务...")
        process = subprocess.Popen([
            "allure", "serve", "report/new_system_temp"
        ])
        
        print("✅ Allure报告服务已启动")
        print("📍 浏览器将自动打开报告页面")
        print("💡 按 Ctrl+C 停止服务")
        
        # 等待用户停止服务
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 停止Allure服务")
            process.terminate()
        
        return True
        
    except FileNotFoundError:
        print("⚠️ Allure服务启动失败，生成静态报告...")
        
        # 生成静态HTML报告
        html_dir = Path("report/new_system_html")
        cmd = [
            "allure", "generate",
            "report/new_system_temp",
            "-o", str(html_dir),
            "--clean"
        ]
        
        result = subprocess.run(cmd)
        if result.returncode == 0:
            html_file = html_dir / "index.html"
            print(f"✅ 静态报告已生成: {html_file.absolute()}")
            
            # 尝试打开浏览器
            try:
                webbrowser.open(f"file://{html_file.absolute()}")
                print("📖 浏览器已打开报告")
            except:
                print("请手动打开报告文件")
            
            return True
        else:
            print("❌ 静态报告生成失败")
            return False

def print_summary():
    """打印测试总结"""
    print("\n" + "="*60)
    print("📊 新系统测试完成")
    print("="*60)
    
    # 检查测试结果文件
    temp_dir = Path("report/new_system_temp")
    if temp_dir.exists():
        result_files = list(temp_dir.glob("*-result.json"))
        print(f"📁 测试数据文件: {len(result_files)} 个")
        
        html_dir = Path("report/new_system_html")
        if html_dir.exists():
            print(f"📄 静态报告: {html_dir / 'index.html'}")
    
    print("\n💡 提示:")
    print("  - 重新查看报告: allure serve report/new_system_temp")
    print("  - 重新运行测试: python run_new_system.py")
    print("  - 只运行失败测试: pytest example_new_system/testcase/ --lf")

def main():
    """主函数"""
    print("🚀 新系统测试启动器")
    print("="*40)
    
    # 1. 检查依赖
    if not check_dependencies():
        print("❌ 依赖检查失败，请安装必要的依赖")
        return 1
    
    # 2. 检查Mock服务器
    if not check_mock_server():
        print("❌ Mock服务器检查失败")
        return 1
    
    # 3. 清理旧报告
    clean_old_reports()
    
    # 4. 运行测试
    test_success = run_tests()
    
    if not test_success:
        print("⚠️ 测试执行完成，但可能有失败的用例")
    else:
        print("✅ 所有测试通过")
    
    # 5. 生成报告
    report_success = generate_allure_report()
    
    if not report_success:
        print("❌ 报告生成失败")
        return 1
    
    # 6. 打印总结
    print_summary()
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n🛑 用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        sys.exit(1)