#!/usr/bin/env python3
"""
Allure报告演示脚本
展示如何生成和查看新系统的Allure报告
"""

import subprocess
import sys
import os
from pathlib import Path
import webbrowser
import time

def create_demo_report():
    """创建演示报告"""
    print("🎯 新系统Allure报告演示")
    print("="*50)
    
    # 1. 收集测试用例并生成基础报告数据
    print("1️⃣ 收集测试用例...")
    
    # 确保报告目录存在
    report_dir = Path("report/new_system_demo")
    report_dir.mkdir(parents=True, exist_ok=True)
    
    # 运行pytest收集测试用例
    cmd = [
        "pytest",
        "example_new_system/testcase/",
        "--collect-only",
        "--alluredir=report/new_system_demo",
        "-q"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ 测试用例收集成功")
        print(f"   收集到的测试用例:")
        lines = result.stdout.split('\n')
        for line in lines:
            if 'collected' in line:
                print(f"   📊 {line.strip()}")
    else:
        print("❌ 测试用例收集失败")
        print(result.stderr)
        return False
    
    # 2. 创建环境信息文件
    print("\n2️⃣ 创建环境信息...")
    env_file = report_dir / "environment.properties"
    env_content = """# 新系统测试环境信息
System.Name=新订单管理系统演示
System.Version=1.0.0
Test.Environment=演示环境
Base.URL=http://127.0.0.1:8787
Test.Framework=pytest + allure
Test.Type=API自动化测试演示
Report.Generated.By=Allure报告演示脚本
Demo.Mode=是
Test.Status=演示模式 - 仅展示报告功能
"""
    
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ 环境信息文件已创建")
    
    # 3. 创建测试分类文件
    print("\n3️⃣ 创建测试分类...")
    categories_file = report_dir / "categories.json"
    categories_content = """[
  {
    "name": "订单管理功能",
    "description": "订单相关的核心功能测试",
    "messageRegex": ".*order.*",
    "traceRegex": ".*TestOrder.*"
  },
  {
    "name": "API接口测试",
    "description": "REST API接口功能验证",
    "messageRegex": ".*api.*",
    "traceRegex": ".*"
  },
  {
    "name": "参数验证测试",
    "description": "接口参数校验和异常处理",
    "messageRegex": ".*参数.*",
    "traceRegex": ".*"
  }
]"""
    
    with open(categories_file, 'w', encoding='utf-8') as f:
        f.write(categories_content)
    
    print("✅ 测试分类文件已创建")
    
    return True

def generate_allure_report():
    """生成Allure报告"""
    print("\n4️⃣ 生成Allure报告...")
    
    try:
        # 检查Allure是否可用
        subprocess.run(["allure", "--version"], capture_output=True, check=True)
        
        # 生成静态HTML报告
        html_dir = Path("report/new_system_demo_html")
        cmd = [
            "allure", "generate",
            "report/new_system_demo",
            "-o", str(html_dir),
            "--clean"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 静态HTML报告生成成功")
            
            # 打开报告
            html_file = html_dir / "index.html"
            if html_file.exists():
                print(f"📄 报告文件: {html_file.absolute()}")
                
                # 尝试打开浏览器
                try:
                    webbrowser.open(f"file://{html_file.absolute()}")
                    print("🌐 浏览器已打开报告")
                except:
                    print("💡 请手动打开报告文件")
                
                return True
            else:
                print("❌ 报告文件未找到")
                return False
        else:
            print("❌ 报告生成失败")
            print(result.stderr)
            return False
            
    except subprocess.CalledProcessError:
        print("❌ Allure未安装或不可用")
        print("💡 请安装Allure: https://docs.qameta.io/allure/")
        return False
    except FileNotFoundError:
        print("❌ Allure命令未找到")
        print("💡 请确保Allure已正确安装并添加到PATH")
        return False

def show_report_features():
    """展示报告功能"""
    print("\n" + "="*60)
    print("📊 Allure报告功能展示")
    print("="*60)
    
    features = [
        "📈 测试执行统计 - 通过/失败/跳过数量和百分比",
        "🎯 测试分类展示 - 按功能模块和优先级分组",
        "📝 测试步骤详情 - 每个测试的详细执行步骤",
        "🔍 失败分析 - 失败原因和错误堆栈信息",
        "📊 趋势分析 - 历史测试结果对比",
        "🏷️ 环境信息 - 测试环境配置和版本信息",
        "⏱️ 执行时间 - 每个测试的耗时统计",
        "🎨 美观界面 - 现代化的Web界面设计",
        "📱 响应式设计 - 支持手机和平板查看",
        "🔗 分享功能 - 可生成静态HTML分享给他人"
    ]
    
    for feature in features:
        print(f"  {feature}")
    
    print(f"\n🎯 报告查看方式:")
    print(f"  📊 实时报告: allure serve report/new_system_demo")
    print(f"  📄 静态报告: 打开 report/new_system_demo_html/index.html")
    
    print(f"\n💡 实际测试命令:")
    print(f"  🧪 运行测试: pytest example_new_system/testcase/ --alluredir=report/new_system_temp -v")
    print(f"  📊 查看报告: allure serve report/new_system_temp")
    print(f"  🚀 一键测试: python run_new_system.py")

def main():
    """主函数"""
    try:
        # 创建演示报告
        if create_demo_report():
            # 生成Allure报告
            if generate_allure_report():
                print("\n✅ Allure报告演示完成！")
            else:
                print("\n⚠️ 报告生成失败，但演示数据已准备好")
                print("💡 你可以手动运行: allure serve report/new_system_demo")
        else:
            print("\n❌ 演示准备失败")
            return 1
        
        # 展示报告功能
        show_report_features()
        
        return 0
        
    except KeyboardInterrupt:
        print("\n🛑 用户中断操作")
        return 1
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())