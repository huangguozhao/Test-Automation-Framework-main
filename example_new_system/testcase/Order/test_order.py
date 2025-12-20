import sys
import os
# 添加项目根目录到Python路径
# 从 example_new_system/testcase/Order/test_order.py 到项目根目录需要向上3级
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.insert(0, project_root)

import allure
import pytest
from common.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from base.generateId import m_id, c_id

@allure.feature(next(m_id) + '订单管理模块')
class TestOrder:

    @allure.story(next(c_id) + "创建订单")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('base_info,testcase', 
                           get_testcase_yaml("./example_new_system/testcase/Order/createOrder.yaml"))
    def test_create_order(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "查询订单")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('base_info,testcase', 
                           get_testcase_yaml("./example_new_system/testcase/Order/queryOrder.yaml"))
    def test_query_order(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)