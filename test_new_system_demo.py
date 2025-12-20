#!/usr/bin/env python3
"""
新系统测试演示脚本
用于验证新系统测试功能
"""

import subprocess
import sys
import os
from pathlib import Path

def test_new_system():
    """测试新系统功能"""
    print("🧪 测试新系统功能...")
    
    # 确保在项目根目录
    os.chdir(Path(__file__).parent)
    
    # 1. 测试收集
    print("1️⃣ 测试用例收集...")
    cmd = ["pytest", "example_new_system/testcase/", "--collect-only", "-q"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ 测试用例收集成功")
        print(result.stdout)
    else:
        print("❌ 测试用例收集失败")
        print(result.stderr)
        return False
    
    # 2. 生成测试报告（不实际运行，只生成结构）
    print("\n2️⃣ 生成Allure报告结构...")
    cmd = [
        "pytest", 
        "example_new_system/testcase/", 
        "--collect-only",
        "--alluredir=report/demo_temp"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ 报告结构生成成功")
    else:
        print("❌ 报告结构生成失败")
        print(result.stderr)
    
    return True

def show_usage_examples():
    """显示使用示例"""
    print("\n" + "="*60)
    print("📚 新系统测试使用示例")
    print("="*60)
    
    examples = [
        ("一键测试脚本", "python run_new_system.py"),
        ("手动测试", "pytest example_new_system/testcase/ -v"),
        ("生成Allure报告", "pytest example_new_system/testcase/ --alluredir=report/new_system_temp -v"),
        ("查看Allure报告", "allure serve report/new_system_temp"),
        ("使用专用配置", "cd example_new_system && pytest"),
        ("并行测试", "pytest example_new_system/testcase/ -n 2 -v"),
        ("失败重试", "pytest example_new_system/testcase/ --reruns 2 -v"),
        ("标记测试", "pytest example_new_system/testcase/ -m smoke -v"),
    ]
    
    for name, cmd in examples:
        print(f"\n🔸 {name}:")
        print(f"   {cmd}")
    
    print(f"\n📁 相关文件:")
    files = [
        "example_new_system/README.md - 新系统说明文档",
        "example_new_system/新系统测试指南.md - 详细测试指南", 
        "example_new_system/pytest.ini - pytest专用配置",
        "example_new_system/environment.properties - Allure环境信息",
        "run_new_system.py - 一键测试脚本"
    ]
    
    for file_desc in files:
        print(f"   📄 {file_desc}")

def main():
    """主函数"""
    print("🚀 新系统测试演示")
    print("="*40)
    
    # 测试功能
    success = test_new_system()
    
    # 显示使用示例
    show_usage_examples()
    
    if success:
        print(f"\n✅ 新系统测试功能验证成功！")
        print(f"💡 现在你可以使用以下命令开始测试:")
        print(f"   python run_new_system.py")
    else:
        print(f"\n❌ 新系统测试功能验证失败")
        print(f"💡 请检查依赖和配置")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())