# 新系统测试自动化框架

这是一个基于pytest + allure的API自动化测试框架，专门用于新系统的接口测试。框架提供了完整的测试解决方案，包括测试用例管理、报告生成、环境配置等功能。

## 🎯 **快速开始**

### **一键测试（推荐）**
```bash
# 运行完整的测试流程
python run_new_system.py
```

### **手动测试**
```bash
# 1. 启动Mock服务器
python mock_server/api_server/base/flask_service.py

# 2. 运行测试
pytest example_new_system/testcase/ --alluredir=report/new_system_temp -v

# 3. 查看Allure报告
allure serve report/new_system_temp
```

## 📁 **项目结构**

```text
├── base/                           # 基础工具类
├── common/                         # 公共模块
├── conf/                           # 配置文件
├── data/                           # 测试数据
├── mock_server/                    # Mock服务器
├── example_new_system/             # 新系统测试示例
│   ├── testcase/Order/            # 订单模块测试
│   ├── config.ini                 # 系统配置
│   ├── loginName.yaml             # 登录配置
│   ├── pytest.ini                # pytest配置
│   └── README.md                  # 详细说明
├── report/                         # 测试报告
│   ├── new_system_temp/           # 新系统测试报告
│   └── new_system_demo/           # 演示报告
├── logs/                          # 日志文件
├── run_new_system.py              # 新系统一键测试脚本
├── demo_allure_report.py          # Allure报告演示
└── 新系统测试快速指南.md          # 快速入门指南
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

## 📊 **测试用例示例**

### **订单管理模块**
- **创建订单**: 正常创建、参数验证、异常处理
- **查询订单**: 订单状态查询、物流状态查询

### **YAML配置示例**
```yaml
- baseInfo:
    api_name: 创建订单
    url: /coupApply/cms/placeAnOrder
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 正常创建订单
      json:
        productId: "12345"
        quantity: 2
        price: 99.99
      validation:
        - contains: { 'msg_code': 200 }
        - contains: { 'msg': '下单成功' }
```

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

## 📚 **文档指南**

- 📄 [新系统测试快速指南](./新系统测试快速指南.md) - 快速入门
- 📄 [框架适配指南](./adaptation_guide.md) - 如何适配新系统
- 📄 [测试启动方法](./test_startup_guide.md) - 多种启动方式
- 📄 [新系统示例说明](./example_new_system/README.md) - 详细示例

## 🎨 **高级功能**

### **并行测试**
```bash
pip install pytest-xdist
pytest example_new_system/testcase/ -n 2 --alluredir=report/new_system_temp
```

### **失败重试**
```bash
pip install pytest-rerunfailures
pytest example_new_system/testcase/ --reruns 2 --alluredir=report/new_system_temp
```

### **标记测试**
```bash
# 只运行冒烟测试
pytest example_new_system/testcase/ -m smoke

# 只运行关键功能
pytest example_new_system/testcase/ -m critical
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

🚀 **立即开始**: `python run_new_system.py`

### 运行测试

使用 uv run 会自动创建虚拟环境，并测试上面的 mock_server 接口, 运行完成后会自动生成 allure 报告

```bash
uv run run.py
```
