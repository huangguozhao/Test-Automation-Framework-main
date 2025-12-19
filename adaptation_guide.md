# 测试框架适配新系统指南

## 🔧 第1步：修改环境配置

### 1.1 修改 `conf/config.ini`
```ini
[api_envi]
host = http://你的系统域名:端口  # 改成你要测试的系统地址

[MYSQL]  # 如果需要数据库断言
host = 你的数据库地址
port = 3306
username = 数据库用户名
password = 数据库密码
database = 数据库名

# 其他数据库配置根据需要修改...
```

### 1.2 修改登录配置 `data/loginName.yaml`
```yaml
- baseInfo:
    api_name: 用户登录
    url: /你的登录接口路径        # 改成你系统的登录接口
    method: post
    header:
      Content-Type: application/json  # 根据你的接口调整
  testCase:
    - case_name: 登录验证
      data:                          # 改成你系统的登录参数
        username: 你的用户名
        password: 你的密码
      validation:                    # 改成你系统的响应格式
        - contains: { 'code': 200 }
        - eq: { 'message': 'success' }
      extract:                       # 提取你需要的token
        token: $.data.token
```

## 📝 第2步：创建测试用例

### 2.1 创建测试模块目录
```bash
mkdir testcase/你的模块名
```

### 2.2 创建接口定义文件 `testcase/你的模块名/接口名.yaml`
```yaml
- baseInfo:
    api_name: 接口名称
    url: /api/your/endpoint
    method: POST
    header:
      Content-Type: application/json
      Authorization: Bearer ${get_extract_data(token)}
  testCase:
    - case_name: 正常场景测试
      json:                          # 或者用data/params
        param1: value1
        param2: value2
      validation:
        - eq: { 'code': 200 }
        - contains: { 'message': 'success' }
      extract:                       # 可选：提取返回值
        orderId: $.data.orderId
    - case_name: 异常场景测试
      json:
        param1: invalid_value
      validation:
        - eq: { 'code': 400 }
```

### 2.3 创建测试执行文件 `testcase/你的模块名/test_your_module.py`
```python
import allure
import pytest
from common.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from base.generateId import m_id, c_id

@allure.feature(next(m_id) + '你的模块名')
class TestYourModule:

    @allure.story(next(c_id) + "功能描述")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('base_info,testcase', 
                           get_testcase_yaml("./testcase/你的模块名/接口名.yaml"))
    def test_your_api(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)
```

## 🔄 第3步：业务流程测试（可选）

如果需要测试业务流程，创建 `testcase/业务流程/流程名.yml`：
```yaml
- baseInfo:
    api_name: 第一个接口
    url: /api/step1
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 步骤1
      json:
        param: value
      validation:
        - eq: { 'code': 200 }
      extract:
        step1_id: $.data.id

- baseInfo:
    api_name: 第二个接口
    url: /api/step2
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 步骤2
      json:
        step1_id: ${get_extract_data(step1_id)}  # 使用上一步的结果
      validation:
        - eq: { 'code': 200 }
```

## 🎯 第4步：运行测试

```bash
# 运行所有测试
python run.py

# 运行指定模块
pytest testcase/你的模块名/ -v

# 生成报告
allure serve report/temp
```

## 💡 高级功能

### 数据驱动测试
```yaml
# 在testCase中添加多个场景
testCase:
  - case_name: 场景1
    json: {param: value1}
    validation: [...]
  - case_name: 场景2  
    json: {param: value2}
    validation: [...]
```

### 动态数据生成
```yaml
json:
  timestamp: ${timestamp()}           # 当前时间戳
  random_id: ${md5_encryption(test)}  # MD5加密
  user_id: ${get_extract_data(userId)} # 提取的数据
```

### 数据库断言
```yaml
validation:
  - db: "SELECT count(*) FROM users WHERE id = '123'"
```

## 📋 检查清单

- [ ] 修改 `conf/config.ini` 中的host地址
- [ ] 修改 `data/loginName.yaml` 登录配置
- [ ] 创建测试模块目录
- [ ] 编写接口定义YAML文件
- [ ] 编写测试执行Python文件
- [ ] 运行测试验证
- [ ] 查看Allure报告

## 🔍 常见问题

1. **接口认证**: 在header中添加Authorization
2. **参数格式**: 根据接口要求选择json/data/params
3. **断言失败**: 检查validation中的字段名和值
4. **数据提取**: 使用正确的JSONPath表达式