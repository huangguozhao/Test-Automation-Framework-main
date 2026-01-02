import allure
import pytest
from common.sendrequest import SendRequest
from common.assertions import Assertions
from common.readyaml import get_testcase_yaml

@allure.epic("淘宝购物系统API测试")
@allure.feature("商品管理")
class TestProductManagement:
    """
    商品管理模块测试 - 使用YAML数据驱动
    """
    
    @pytest.mark.parametrize("case_data", get_testcase_yaml("testcase/taobao/product.yaml"))
    def test_product_api(self, case_data):
        """
        商品管理接口测试
        """
        # 检查数据结构并正确获取测试用例信息
        if isinstance(case_data, list) and len(case_data) == 2:
            # 框架转换后的格式 [base_info, test_case]
            base_info = case_data[0]
            test_case = case_data[1]
        elif isinstance(case_data, dict) and 'baseInfo' in case_data:
            # 原始YAML格式
            base_info = case_data['baseInfo']
            # 遍历所有测试用例
            for test_case in case_data['testCase']:
                self._run_test_case(base_info, test_case)
            return
        else:
            pytest.fail(f"不支持的数据格式: {type(case_data)}")
        
        # 执行单个测试用例
        self._run_test_case(base_info, test_case)
    
    def _run_test_case(self, base_info, test_case):
        """
        执行单个测试用例
        """
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
            params=test_case.get("params", {})
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
