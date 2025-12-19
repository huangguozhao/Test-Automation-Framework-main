# 新系统适配示例

假设你要测试一个电商系统，以下是完整的适配示例。

## 系统信息
- 系统地址: http://api.example.com
- 登录接口: POST /api/v1/auth/login
- 需要JWT Token认证

## 文件清单
1. conf/config.ini - 环境配置
2. data/loginName.yaml - 登录配置
3. testcase/Order/ - 订单模块测试
   - createOrder.yaml - 创建订单接口
   - queryOrder.yaml - 查询订单接口
   - test_order.py - 测试执行文件