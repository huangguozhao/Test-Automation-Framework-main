# API自动化测试框架完整使用指南

## 📋 目录
- [框架概述](#框架概述)
- [环境准备](#环境准备)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [测试用例编写](#测试用例编写)
- [断言配置](#断言配置)
- [高级功能](#高级功能)
- [报告生成](#报告生成)
- [最佳实践](#最佳实践)
- [常见问题](#常见问题)

## 🎯 框架概述

这是一个基于 **pytest + allure** 的API自动化测试框架，具有以下特点：

### 核心特性
- ✅ **YAML驱动**: 使用YAML文件定义测试用例，易于维护和扩展
- ✅ **参数化测试**: 支持多种测试场景和数据驱动测试
- ✅ **丰富断言**: 支持多种断言方式（包含、相等、不等、JSONPath等）
- ✅ **数据提取**: 支持JSONPath和正则表达式提取响应数据
- ✅ **美观报告**: 集成Allure生成详细的HTML测试报告
- ✅ **环境隔离**: 支持多环境配置切换
- ✅ **Mock服务**: 内置Mock服务器，支持离线测试

### 适用场景
- REST API接口测试
- 微服务接口测试
- 第三方API集成测试
- 回归测试自动化
- 持续集成/持续部署(CI/CD)

## 🛠️ 环境准备

### Python环境
```bash
# Python 3.8+ 
python --version

# 安装依赖
pip install pytest allure-pytest requests pyyaml jsonpath-ng
```

### Allure安装
```bash
# Windows (使用Scoop)
scoop install allure

# macOS (使用Homebrew)
brew install allure

# 或者下载安装包
# https://allurereport.org/docs/install-for-windows/
```

### 验证安装
```bash
pytest --version
allure --version
```

## 📁 项目结构

```text
Test-Automation-Framework/
├── base/                           # 基础工具类
│   ├── apiutil.py                 # API工具类
│   ├── generateId.py              # ID生成工具
│   └── new_testcase_tools.py      # 测试用例工具
├── common/                         # 公共模块
│   ├── assertions.py              # 断言模块
│   ├── sendrequest.py             # 请求发送模块
│   ├── readyaml.py                # YAML读取模块
│   ├── recordlog.py               # 日志记录模块
│   └── ...                        # 其他工具模块
├── conf/                           # 配置文件
├── data/                           # 测试数据
├── testcase/                       # 测试用例目录
│   ├── __init__.py                # Python包标识
│   ├── conftest.py                # pytest配置
│   ├── extract.yaml               # 数据提取配置
│   └── [你的测试模块]/            # 具体测试模块
│       ├── test_*.py              # Python测试文件
│       └── *.yaml                 # YAML测试用例
├── report/                         # 测试报告
├── logs/                          # 日志文件
├── mock_server/                    # Mock服务器
├── pytest.ini                     # pytest配置
├── run.py                         # 主运行脚本
└── README.md                      # 项目说明
```

## 🚀 快速开始

### 1. 创建测试模块

在 `testcase/` 目录下创建你的测试模块：

```bash
mkdir testcase/YourSystem
```

### 2. 编写YAML测试用例

创建 `testcase/YourSystem/api_tests.yaml`：

```yaml
- baseInfo:
    api_name: 获取用户列表
    url: https://your-api.com/users
    method: GET
    header:
      Content-Type: application/json
      Authorization: Bearer your-token
  testCase:
    - case_name: 正常获取用户列表
      validation:
        - eq: { '$.status_code': 200 }
        - contains: { '$.json()[0].id': 1 }

- baseInfo:
    api_name: 创建用户
    url: https://your-api.com/users
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 创建用户成功
      json:
        name: "测试用户"
        email: "test@example.com"
      validation:
        - eq: { '$.status_code': 201 }
        - contains: { '$.json().name': '测试用户' }
```

### 3. 编写Python测试文件

创建 `testcase/YourSystem/test_api.py`：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from common.readyaml import get_testcase_yaml
from common.sendrequest import SendRequest
from common.assertions import Assertions


@allure.epic("YourSystem API测试")
@allure.feature("用户管理")
class TestYourSystemAPI:
    """YourSystem API接口测试"""

    @pytest.mark.parametrize("case_data", get_testcase_yaml("testcase/YourSystem/api_tests.yaml"))
    def test_api(self, case_data):
        """
        API接口测试
        """
        # 检查数据结构并正确获取测试用例信息
        if isinstance(case_data, list) and len(case_data) == 2:
            # 框架转换后的格式 [base_info, test_case]
            base_info = case_data[0]
            test_case = case_data[1]
        elif isinstance(case_data, dict) and 'baseInfo' in case_data:
            # 原始YAML格式
            base_info = case_data['baseInfo']
            # 取第一个测试用例
            test_case = case_data['testCase'][0]
        else:
            pytest.fail(f"不支持的数据格式: {type(case_data)}")
        
        # 设置Allure报告信息
        allure.dynamic.story(base_info["api_name"])
        allure.dynamic.title(f"{base_info['api_name']} - {test_case['case_name']}")
        
        # 发送请求
        send_request = SendRequest()
        response = send_request.send_request(
            method=base_info["method"],
            url=base_info["url"],
            headers=base_info.get("header", {}),
            json=test_case.get("json", {}),
            params=test_case.get("params", {}),
            data=test_case.get("data", {})
        )
        
        # 添加请求和响应信息到Allure报告
        with allure.step("请求信息"):
            allure.attach(f"URL: {base_info['url']}", "请求URL", allure.attachment_type.TEXT)
            allure.attach(f"Method: {base_info['method']}", "请求方法", allure.attachment_type.TEXT)
            if test_case.get("json"):
                allure.attach(str(test_case["json"]), "请求体", allure.attachment_type.JSON)
        
        with allure.step("响应信息"):
            allure.attach(f"状态码: {response.status_code}", "响应状态码", allure.attachment_type.TEXT)
            allure.attach(response.text, "响应内容", allure.attachment_type.JSON)
        
        # 执行断言
        assertions = Assertions()
        with allure.step("执行断言验证"):
            for validation in test_case.get("validation", []):
                assertions.assert_response_any(response, validation)
```

### 4. 运行测试

```bash
# 运行测试并生成Allure报告
pytest testcase/YourSystem/ --alluredir=report/temp -v

# 查看Allure报告
allure serve report/temp
```

## 📝 测试用例编写

### YAML文件结构

```yaml
- baseInfo:                         # 接口基本信息
    api_name: 接口名称              # 接口描述名称
    url: http://api.example.com     # 接口URL
    method: GET                     # 请求方法 (GET/POST/PUT/DELETE等)
    header:                         # 请求头 (可选)
      Content-Type: application/json
      Authorization: Bearer token
  testCase:                         # 测试用例列表
    - case_name: 测试用例名称       # 用例描述
      json:                         # JSON请求体 (POST/PUT时使用)
        key: value
      params:                       # URL参数 (可选)
        page: 1
        size: 10
      data:                         # 表单数据 (可选)
        username: test
      validation:                   # 断言列表
        - eq: { '$.status_code': 200 }
        - contains: { '$.json().message': 'success' }
```

### 请求参数类型

#### 1. JSON请求体 (json)
```yaml
json:
  name: "用户名"
  age: 25
  email: "user@example.com"
```

#### 2. URL参数 (params)
```yaml
params:
  page: 1
  size: 20
  keyword: "搜索关键词"
```

#### 3. 表单数据 (data)
```yaml
data:
  username: "admin"
  password: "123456"
```

#### 4. 请求头 (header)
```yaml
header:
  Content-Type: application/json
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  X-Custom-Header: custom-value
```

### 多测试用例示例

```yaml
- baseInfo:
    api_name: 用户登录
    url: https://api.example.com/login
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 正常登录
      json:
        username: "admin"
        password: "123456"
      validation:
        - eq: { '$.status_code': 200 }
        - contains: { '$.json().message': '登录成功' }
    
    - case_name: 用户名错误
      json:
        username: "wrong_user"
        password: "123456"
      validation:
        - eq: { '$.status_code': 401 }
        - contains: { '$.json().message': '用户名或密码错误' }
    
    - case_name: 密码错误
      json:
        username: "admin"
        password: "wrong_pass"
      validation:
        - eq: { '$.status_code': 401 }
        - contains: { '$.json().message': '用户名或密码错误' }
```

## ✅ 断言配置

### 断言类型

#### 1. 相等断言 (eq)
```yaml
validation:
  - eq: { '$.status_code': 200 }           # 状态码等于200
  - eq: { '$.json().id': 1 }               # 响应JSON中id等于1
  - eq: { '$.json().user.name': 'admin' }  # 嵌套字段断言
```

#### 2. 包含断言 (contains)
```yaml
validation:
  - contains: { '$.json().message': '成功' }     # 消息包含"成功"
  - contains: { '$.text': 'success' }           # 响应文本包含"success"
  - contains: { '$.json().data[0].name': 'test' } # 数组元素断言
```

#### 3. 不等断言 (ne)
```yaml
validation:
  - ne: { '$.status_code': 500 }           # 状态码不等于500
  - ne: { '$.json().error': null }         # error字段不为null
```

#### 4. 大于/小于断言 (gt/lt)
```yaml
validation:
  - gt: { '$.json().count': 0 }            # count大于0
  - lt: { '$.json().total': 1000 }         # total小于1000
```

### JSONPath表达式

#### 基本语法
```yaml
# 根节点
'$.status_code'                    # HTTP状态码
'$.text'                          # 响应文本
'$.json()'                        # 整个JSON响应

# 对象属性
'$.json().message'                # 获取message字段
'$.json().data.user.name'         # 嵌套对象属性

# 数组操作
'$.json()[0]'                     # 第一个元素
'$.json()[0].id'                  # 第一个元素的id
'$.json().data[*].name'           # 所有元素的name字段
```

#### 复杂示例
```yaml
# 响应示例
{
  "code": 200,
  "message": "success",
  "data": {
    "users": [
      {"id": 1, "name": "Alice", "age": 25},
      {"id": 2, "name": "Bob", "age": 30}
    ],
    "total": 2
  }
}

# 对应断言
validation:
  - eq: { '$.json().code': 200 }
  - contains: { '$.json().message': 'success' }
  - eq: { '$.json().data.total': 2 }
  - eq: { '$.json().data.users[0].name': 'Alice' }
  - gt: { '$.json().data.users[1].age': 25 }
```

## 🔧 高级功能

### 1. 环境配置

创建 `conf/config.ini`：

```ini
[test]
base_url = https://test-api.example.com
username = test_user
password = test_pass

[prod]
base_url = https://api.example.com
username = prod_user
password = prod_pass
```

在测试中使用：

```python
from conf.operationConfig import OperationConfig

config = OperationConfig()
base_url = config.get_config('test', 'base_url')
```

### 2. 数据提取和关联

#### 提取响应数据
```yaml
# 在第一个接口中提取token
- baseInfo:
    api_name: 用户登录
    url: https://api.example.com/login
    method: POST
  testCase:
    - case_name: 登录获取token
      json:
        username: "admin"
        password: "123456"
      extract:
        token: $.json().token        # 提取token到变量
      validation:
        - eq: { '$.status_code': 200 }

# 在后续接口中使用提取的数据
- baseInfo:
    api_name: 获取用户信息
    url: https://api.example.com/user/profile
    method: GET
    header:
      Authorization: Bearer ${token}  # 使用提取的token
  testCase:
    - case_name: 获取个人信息
      validation:
        - eq: { '$.status_code': 200 }
```

### 3. 参数化测试

#### 使用pytest参数化
```python
@pytest.mark.parametrize("user_data", [
    {"username": "user1", "expected_code": 200},
    {"username": "user2", "expected_code": 200},
    {"username": "invalid", "expected_code": 404}
])
def test_get_user(self, user_data):
    # 测试逻辑
    pass
```

#### 使用YAML数据驱动
```yaml
- baseInfo:
    api_name: 批量用户测试
    url: https://api.example.com/users/{user_id}
    method: GET
  testCase:
    - case_name: 用户1
      path_params:
        user_id: 1
      validation:
        - eq: { '$.status_code': 200 }
    
    - case_name: 用户2
      path_params:
        user_id: 2
      validation:
        - eq: { '$.status_code': 200 }
```

### 4. Mock服务器使用

#### 启动内置Mock服务器
```bash
python mock_server/api_server/base/flask_service.py
```

#### 配置Mock接口
```python
# 在mock_server中添加自定义接口
@app.route('/api/custom', methods=['POST'])
def custom_api():
    return jsonify({
        "code": 200,
        "message": "success",
        "data": {"id": 1, "name": "test"}
    })
```

## 📊 报告生成

### 1. 生成Allure报告

```bash
# 运行测试并生成报告数据
pytest testcase/ --alluredir=report/allure-results -v

# 启动Allure服务查看报告
allure serve report/allure-results

# 生成静态HTML报告
allure generate report/allure-results -o report/allure-report --clean
```

### 2. 报告定制

#### 添加环境信息
创建 `report/allure-results/environment.properties`：

```properties
Environment=Test
API.Base.URL=https://test-api.example.com
Browser=Chrome
Test.Framework=pytest + allure
```

#### 添加测试分类
```python
@allure.epic("电商系统")           # 史诗级别
@allure.feature("用户管理")        # 功能级别
@allure.story("用户注册")          # 用户故事级别
@allure.severity(allure.severity_level.CRITICAL)  # 严重程度
@allure.tag("smoke", "regression")  # 标签
def test_user_register(self):
    pass
```

### 3. 报告截图和附件

```python
# 添加截图
allure.attach.file("screenshot.png", attachment_type=allure.attachment_type.PNG)

# 添加文本
allure.attach("测试数据", "附加信息", allure.attachment_type.TEXT)

# 添加JSON
allure.attach(json.dumps(response_data), "响应数据", allure.attachment_type.JSON)
```

## 🎯 最佳实践

### 1. 项目组织

```text
testcase/
├── common_apis/              # 公共接口测试
│   ├── test_auth.py         # 认证相关
│   └── auth.yaml
├── user_module/             # 用户模块
│   ├── test_user_crud.py    # 用户CRUD操作
│   ├── user_crud.yaml
│   ├── test_user_profile.py # 用户资料
│   └── user_profile.yaml
└── order_module/            # 订单模块
    ├── test_order_flow.py   # 订单流程
    └── order_flow.yaml
```

### 2. 命名规范

#### 文件命名
- YAML文件：`模块名_功能.yaml`
- Python文件：`test_模块名_功能.py`
- 类名：`Test模块名功能`

#### 用例命名
```yaml
- baseInfo:
    api_name: 用户管理-创建用户      # 模块-功能
  testCase:
    - case_name: 正常创建用户-所有必填字段    # 场景描述
    - case_name: 异常创建用户-缺少必填字段
    - case_name: 边界测试-用户名长度限制
```

### 3. 数据管理

#### 测试数据分离
```text
data/
├── test_users.json          # 测试用户数据
├── test_products.json       # 测试商品数据
└── environments/
    ├── test.yaml           # 测试环境配置
    └── prod.yaml           # 生产环境配置
```

#### 敏感数据处理
```python
import os

# 使用环境变量
api_key = os.getenv('API_KEY', 'default_key')
password = os.getenv('TEST_PASSWORD', 'default_pass')
```

### 4. 错误处理

```python
def test_api_with_retry(self):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = send_request.send_request(...)
            # 断言逻辑
            break
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(2)  # 重试间隔
```

### 5. 并行执行

```bash
# 安装pytest-xdist
pip install pytest-xdist

# 并行运行测试
pytest testcase/ -n 4 --alluredir=report/temp
```

## ❓ 常见问题

### 1. 导入模块错误

**问题**: `ModuleNotFoundError: No module named 'common'`

**解决方案**:
```python
# 在测试文件顶部添加
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

### 2. JSONPath断言失败

**问题**: JSONPath表达式无法匹配数据

**解决方案**:
```python
# 调试JSONPath表达式
import jsonpath
response_json = response.json()
result = jsonpath.jsonpath(response_json, '$.data.users[0].name')
print(f"JSONPath结果: {result}")
```

### 3. 请求超时

**问题**: 接口请求超时

**解决方案**:
```python
# 在SendRequest中设置超时
response = send_request.send_request(
    method="GET",
    url="https://api.example.com/slow-api",
    timeout=30  # 30秒超时
)
```

### 4. 证书验证错误

**问题**: SSL证书验证失败

**解决方案**:
```python
# 禁用SSL验证（仅测试环境）
response = send_request.send_request(
    method="GET",
    url="https://api.example.com",
    verify=False
)
```

### 5. 中文编码问题

**问题**: 中文字符显示乱码

**解决方案**:
```yaml
# 确保YAML文件使用UTF-8编码保存
# 在Python文件头部添加
# -*- coding: utf-8 -*-
```

### 6. Allure报告不显示

**问题**: 生成的报告为空或不显示

**解决方案**:
```bash
# 检查报告目录权限
chmod -R 755 report/

# 清理旧报告
rm -rf report/allure-results/*
pytest testcase/ --alluredir=report/allure-results --clean-alluredir
```

## 🔗 相关资源

### 官方文档
- [Pytest官方文档](https://docs.pytest.org/)
- [Allure官方文档](https://allurereport.org/)
- [Requests库文档](https://requests.readthedocs.io/)

### 扩展插件
- `pytest-html`: 生成HTML测试报告
- `pytest-xdist`: 并行测试执行
- `pytest-rerunfailures`: 失败用例重试
- `pytest-mock`: Mock功能增强

### JSONPath工具
- [JSONPath在线测试](https://jsonpath.com/)
- [JSONPath语法参考](https://goessner.net/articles/JsonPath/)

---

## 📞 技术支持

如果在使用过程中遇到问题，可以：

1. 查看项目日志文件 `logs/`
2. 检查pytest配置 `pytest.ini`
3. 参考示例测试用例 `testcase/JSONPlaceholder/`
4. 查看框架源码了解实现细节

**祝你测试愉快！** 🎉