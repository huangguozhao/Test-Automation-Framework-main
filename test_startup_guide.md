# 测试启动方法大全

## 🎯 **启动测试的多种方法**

### **方法1：使用框架启动脚本（推荐）**
```bash
# 启动完整测试流程（包含Allure报告）
python run.py
```
**特点：**
- ✅ 自动生成Allure报告
- ✅ 自动打开浏览器查看报告
- ✅ 包含完整的测试流程

### **方法2：直接使用pytest命令**
```bash
# 运行所有测试
pytest

# 运行指定目录的测试
pytest testcase/

# 运行指定文件的测试
pytest testcase/Single\ interface/test_debug_api.py

# 运行指定测试类
pytest testcase/Single\ interface/test_debug_api.py::TestUserManager

# 运行指定测试方法
pytest testcase/Single\ interface/test_debug_api.py::TestUserManager::test_add_user

# 显示详细输出
pytest -v

# 显示print输出
pytest -s

# 生成Allure报告
pytest --alluredir=report/temp

# 组合参数
pytest -vs --alluredir=report/temp testcase/
```

### **方法3：运行特定模块测试**
```bash
# 只运行用户管理模块
pytest testcase/Single\ interface/ -v

# 只运行商品管理模块  
pytest testcase/ProductManager/ -v

# 只运行业务流程测试
pytest testcase/Business\ interface/ -v
```

### **方法4：按标记运行测试**
```bash
# 运行指定order的测试
pytest -m "order==1" -v

# 运行特定story的测试
pytest -k "新增用户" -v

# 运行包含特定关键字的测试
pytest -k "user" -v
```

### **方法5：生成不同类型的报告**
```bash
# 生成Allure报告
pytest --alluredir=report/temp
allure serve report/temp

# 生成HTML报告
pytest --html=report/report.html --self-contained-html

# 生成JUnit XML报告
pytest --junitxml=report/junit.xml

# 生成覆盖率报告
pytest --cov=common --cov-report=html
```

### **方法6：调试模式运行**
```bash
# 在第一个失败时停止
pytest -x

# 在N个失败后停止
pytest --maxfail=2

# 显示最慢的10个测试
pytest --durations=10

# 只运行失败的测试
pytest --lf

# 运行失败的测试和新增的测试
pytest --ff
```

## 🔧 **新系统测试启动步骤**

### **步骤1：准备环境**
```bash
# 1. 修改配置文件
# 编辑 conf/config.ini 中的host地址
# 编辑 data/loginName.yaml 中的登录信息

# 2. 安装依赖（如果需要）
pip install -r requirements.txt
```

### **步骤2：创建测试用例**
```bash
# 1. 创建测试目录
mkdir testcase/你的模块名

# 2. 创建YAML接口定义文件
# 创建 testcase/你的模块名/接口名.yaml

# 3. 创建Python测试执行文件  
# 创建 testcase/你的模块名/test_模块名.py
```

### **步骤3：运行测试**
```bash
# 测试单个接口
pytest testcase/你的模块名/test_模块名.py::TestClass::test_method -v

# 测试整个模块
pytest testcase/你的模块名/ -v

# 生成报告
python run.py
```

## 🎨 **高级启动技巧**

### **并行执行测试**
```bash
# 安装pytest-xdist
pip install pytest-xdist

# 并行运行测试
pytest -n 4  # 使用4个进程

# 自动检测CPU核心数
pytest -n auto
```

### **重试失败的测试**
```bash
# 安装pytest-rerunfailures
pip install pytest-rerunfailures

# 失败时重试3次
pytest --reruns 3

# 重试间隔2秒
pytest --reruns 3 --reruns-delay 2
```

### **参数化运行**
```bash
# 使用环境变量
export TEST_ENV=staging
pytest

# 使用pytest参数
pytest --env=production

# 使用配置文件
pytest -c custom_pytest.ini
```

## 📊 **报告查看方式**

### **Allure报告**
```bash
# 生成并查看报告
pytest --alluredir=report/temp
allure serve report/temp

# 生成静态报告
allure generate report/temp -o report/allure-report --clean
```

### **实时监控**
```bash
# 监控文件变化自动运行测试
pip install pytest-watch
ptw testcase/
```

## 🚨 **常见问题解决**

### **依赖问题**
```bash
# jsonpath问题
pip uninstall jsonpath
pip install jsonpath-ng

# allure问题  
# Windows: 下载allure并配置环境变量
# Mac: brew install allure
```

### **编码问题**
```bash
# 设置环境变量
set PYTHONIOENCODING=utf-8
pytest
```

### **路径问题**
```bash
# 使用绝对路径
pytest E:/myProject/Test-Automation-Framework-main/testcase/

# 或者切换到项目目录
cd E:/myProject/Test-Automation-Framework-main
pytest testcase/
```

## 💡 **最佳实践**

1. **开发阶段**: 使用 `pytest -v` 快速验证
2. **调试阶段**: 使用 `pytest -vs --tb=short` 查看详细信息  
3. **CI/CD**: 使用 `python run.py` 生成完整报告
4. **性能测试**: 使用 `pytest --durations=10` 找出慢测试
5. **回归测试**: 使用 `pytest --lf` 只运行失败的测试

## 🎯 **针对新系统的快速启动**

```bash
# 1. 快速验证配置
pytest testcase/你的模块名/ -v --tb=short

# 2. 生成完整报告
python run.py

# 3. 只运行成功的测试
pytest --lf -v

# 4. 调试特定测试
pytest testcase/你的模块名/test_xxx.py::test_method -vs
```