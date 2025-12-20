# API自动化测试框架

这是一个基于pytest + allure的API自动化测试框架，提供了完整的测试解决方案，包括测试用例管理、报告生成、环境配置等功能。

## 🎯 **快速开始**

### **基础测试**
```bash
# 1. 启动Mock服务器
python mock_server/api_server/base/flask_service.py

# 2. 运行测试（需要先创建测试用例）
pytest testcase/ --alluredir=report/temp -v

# 3. 查看Allure报告
allure serve report/temp
```

### **使用uv运行**
```bash
# 使用uv自动管理依赖和虚拟环境
uv run run.py
```

## 📁 **项目结构**

```text
├── base/                           # 基础工具类
├── common/                         # 公共模块
├── conf/                           # 配置文件
├── data/                           # 测试数据
├── mock_server/                    # Mock服务器
├── testcase/                       # 测试用例目录（空）
│   ├── __init__.py                # Python包标识
│   ├── conftest.py                # pytest配置
│   └── extract.yaml               # 数据提取配置
├── report/                         # 测试报告
├── logs/                          # 日志文件
├── run.py                         # 主运行脚本
├── pytest.ini                    # pytest配置
└── adaptation_guide.md            # 框架适配指南
```

## 🚀 **核心功能**

### **测试框架特性**
- ✅ **YAML驱动**: 使用YAML文件定义测试用例，易于维护
- ✅ **参数化测试**: 支持多种测试场景和数据驱动
- ✅ **断言丰富**: 支持多种断言方式（包含、相等、不等等）
- ✅ **数据提取**: 支持JSONPath和正则表达式提取
- ✅ **环境隔离**: 支持多环境配置切换

### **Allure报告功能**
- 📊 **美观报告**: 现代化Web界面，支持移动端
- 📈 **详细统计**: 测试通过率、执行时间、趋势分析
- 🎯 **分类管理**: 按功能模块、优先级分组
- 🔍 **失败分析**: 详细的错误信息和堆栈跟踪
- 🏷️ **环境信息**: 自动显示测试环境配置

### **Mock服务器**
- 🔧 **完整API**: 提供用户管理、订单管理等接口
- 🎲 **模拟数据**: 无需真实环境，支持各种测试场景
- 🚀 **快速启动**: 一键启动，支持热重载

## 🛠️ **环境要求**

### **Python依赖**
```bash
pip install pytest allure-pytest requests pyyaml
```

### **Allure安装**
```bash
# Mac
brew install allure

# Windows
# 下载并安装: https://allurereport.org/docs/install-for-windows/
```

## 📚 **使用指南**

### **创建测试用例**
1. 在 `testcase/` 目录下创建模块文件夹
2. 编写YAML测试用例文件
3. 编写对应的Python测试文件
4. 参考 `adaptation_guide.md` 了解详细步骤

### **YAML配置示例**
```yaml
- baseInfo:
    api_name: 示例接口
    url: /api/example
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 正常请求
      json:
        param1: "value1"
        param2: "value2"
      validation:
        - contains: { 'code': 200 }
        - contains: { 'msg': '成功' }
```

## 🎨 **高级功能**

### **并行测试**
```bash
pip install pytest-xdist
pytest testcase/ -n 2 --alluredir=report/temp
```

### **失败重试**
```bash
pip install pytest-rerunfailures
pytest testcase/ --reruns 2 --alluredir=report/temp
```

### **标记测试**
```bash
# 只运行冒烟测试
pytest testcase/ -m smoke

# 只运行关键功能
pytest testcase/ -m critical
```

## 🆘 **常见问题**

### **Q: Mock服务器启动失败？**
A: 检查端口8787是否被占用，或修改配置文件中的端口

### **Q: 找不到模块错误？**
A: 确保在项目根目录运行命令，或使用绝对路径

### **Q: Allure报告无法生成？**
A: 检查Allure是否正确安装，或使用静态报告模式

## 🤝 **贡献指南**

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 **许可证**

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

🚀 **立即开始**: 查看 `adaptation_guide.md` 了解如何创建你的第一个测试用例
