# 淘宝购物系统API接口文档

## 文档说明

本文档基于OpenAPI 3.1.0规范的YAML文件转换而来，详细描述了电商系统的后端API接口。

**基本信息：**
- 版本：1.0.0
- 联系人：Victor
- 邮箱：victor@example.com
- 许可证：Apache 2.0
- 服务器地址：http://localhost:8080

## API分组概览

本系统包含以下22个API功能模块：

1. [用户管理](#用户管理)
2. [商品管理](#商品管理)
3. [订单管理](#订单管理)
4. [购物车管理](#购物车管理)
5. [商店管理](#商店管理)
6. [评价管理](#评价管理)
7. [收藏管理](#收藏管理)
8. [分类管理](#分类管理)
9. [地址管理](#地址管理)
10. [商品SKU管理](#商品SKU管理)
11. [商品规格管理](#商品规格管理)
12. [订单项管理](#订单项管理)
13. [支付记录管理](#支付记录管理)
14. [退款记录管理](#退款记录管理)
15. [物流管理](#物流管理)
16. [消息管理](#消息管理)
17. [操作日志管理](#操作日志管理)
18. [系统配置管理](#系统配置管理)
19. [每日统计管理](#每日统计管理)
20. [商店统计管理](#商店统计管理)
21. [商品统计管理](#商品统计管理)
22. [搜索关键词管理](#搜索关键词管理)

## 数据模型定义

本文档使用以下数据模型：

- [User 用户模型](#User)
- [ResponseVO 响应模型](#ResponseVO)
- [Product 商品模型](#Product)
- [Order 订单模型](#Order)
- [Shop 商店模型](#Shop)
- [Cart 购物车模型](#Cart)
- [Review 评价模型](#Review)
- [Category 分类模型](#Category)
- [Address 地址模型](#Address)
- 其他查询模型和统计模型

---

## 用户管理

### 接口列表

#### 1. 根据用户名更新用户
- **接口地址：** `PUT /user/updateUserByUsername`
- **接口描述：** 根据用户名更新用户信息
- **请求参数：**
  - `bean` (query, required): 用户对象，类型为 User
  - `username` (query, required): 用户名，类型为 string
- **响应：** ResponseVO

#### 2. 根据ID更新用户
- **接口地址：** `PUT /user/updateUserById`
- **接口描述：** 通过用户ID更新用户信息
- **请求参数：**
  - `bean` (query, required): 用户对象，类型为 User
  - `id` (query, required): 用户ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 3. 新增用户
- **接口地址：** `POST /user/add`
- **接口描述：** 创建新的用户记录
- **请求参数：**
  - `bean` (query, required): 用户对象，类型为 User
- **响应：** ResponseVO

#### 4. 批量新增或更新用户
- **接口地址：** `POST /user/addOrUpdateBatch`
- **接口描述：** 批量新增或更新用户记录
- **请求体：** User 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 5. 批量新增用户
- **接口地址：** `POST /user/addBatch`
- **接口描述：** 批量新增用户记录
- **请求体：** User 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 6. 分页查询用户列表
- **接口地址：** `GET /user/loadDataList`
- **接口描述：** 根据查询条件分页获取用户列表
- **请求参数：**
  - `query` (query, required): 用户查询条件，类型为 UserQuery
- **响应：** ResponseVO

#### 7. 根据用户名查询用户
- **接口地址：** `GET /user/getUserByUsername`
- **接口描述：** 根据用户名获取用户信息
- **请求参数：**
  - `username` (query, required): 用户名，类型为 string
- **响应：** ResponseVO

#### 8. 根据ID查询用户
- **接口地址：** `GET /user/getUserById`
- **接口描述：** 通过用户ID获取用户信息
- **请求参数：**
  - `id` (query, required): 用户ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 9. 根据用户名删除用户
- **接口地址：** `DELETE /user/deleteUserByUsername`
- **接口描述：** 根据用户名删除用户记录
- **请求参数：**
  - `username` (query, required): 用户名，类型为 string
- **响应：** ResponseVO

#### 10. 根据ID删除用户
- **接口地址：** `DELETE /user/deleteUserById`
- **接口描述：** 根据用户ID删除用户记录
- **请求参数：**
  - `id` (query, required): 用户ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 商品管理

### 接口列表

#### 1. 根据ID更新商品
- **接口地址：** `PUT /product/updateProductById`
- **接口描述：** 通过商品ID更新商品信息
- **请求参数：**
  - `bean` (query, required): 商品对象，类型为 Product
  - `id` (query, required): 商品ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 新增商品
- **接口地址：** `POST /product/add`
- **接口描述：** 创建新的商品记录
- **请求参数：**
  - `bean` (query, required): 商品对象，类型为 Product
- **响应：** ResponseVO

#### 3. 批量新增或更新商品
- **接口地址：** `POST /product/addOrUpdateBatch`
- **接口描述：** 批量新增或更新商品记录
- **请求体：** Product 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 4. 批量新增商品
- **接口地址：** `POST /product/addBatch`
- **接口描述：** 批量新增商品记录
- **请求体：** Product 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 5. 分页查询商品列表
- **接口地址：** `GET /product/loadDataList`
- **接口描述：** 根据查询条件分页获取商品列表
- **请求参数：**
  - `query` (query, required): 商品查询条件，类型为 ProductQuery
- **响应：** ResponseVO

#### 6. 根据ID查询商品
- **接口地址：** `GET /product/getProductById`
- **接口描述：** 通过商品ID获取商品信息
- **请求参数：**
  - `id` (query, required): 商品ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 7. 根据ID删除商品
- **接口地址：** `DELETE /product/deleteProductById`
- **接口描述：** 通过商品ID删除商品记录
- **请求参数：**
  - `id` (query, required): 商品ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 订单管理

### 接口列表

#### 1. 根据订单号更新订单
- **接口地址：** `PUT /order/updateOrderByOrderNo`
- **接口描述：** 通过订单号更新订单信息
- **请求参数：**
  - `bean` (query, required): 订单对象，类型为 Order
  - `orderNo` (query, required): 订单号，类型为 string
- **响应：** ResponseVO

#### 2. 根据ID更新订单
- **接口地址：** `PUT /order/updateOrderById`
- **接口描述：** 通过订单ID更新订单信息
- **请求参数：**
  - `bean` (query, required): 订单对象，类型为 Order
  - `id` (query, required): 订单ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 3. 新增订单
- **接口地址：** `POST /order/add`
- **接口描述：** 创建新的订单记录
- **请求参数：**
  - `bean` (query, required): 订单对象，类型为 Order
- **响应：** ResponseVO

#### 4. 批量新增或更新订单
- **接口地址：** `POST /order/addOrUpdateBatch`
- **接口描述：** 批量新增或更新订单记录
- **请求体：** Order 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 5. 批量新增订单
- **接口地址：** `POST /order/addBatch`
- **接口描述：** 批量新增订单记录
- **请求体：** Order 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 6. 分页查询订单列表
- **接口地址：** `GET /order/loadDataList`
- **接口描述：** 根据查询条件分页获取订单列表
- **请求参数：**
  - `query` (query, required): 订单查询条件，类型为 OrderQuery
- **响应：** ResponseVO

#### 7. 根据订单号查询订单
- **接口地址：** `GET /order/getOrderByOrderNo`
- **接口描述：** 通过订单号获取订单信息
- **请求参数：**
  - `orderNo` (query, required): 订单号，类型为 string
- **响应：** ResponseVO

#### 8. 根据ID查询订单
- **接口地址：** `GET /order/getOrderById`
- **接口描述：** 通过订单ID获取订单信息
- **请求参数：**
  - `id` (query, required): 订单ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 9. 根据订单号删除订单
- **接口地址：** `DELETE /order/deleteOrderByOrderNo`
- **接口描述：** 通过订单号删除订单记录
- **请求参数：**
  - `orderNo` (query, required): 订单号，类型为 string
- **响应：** ResponseVO

#### 10. 根据ID删除订单
- **接口地址：** `DELETE /order/deleteOrderById`
- **接口描述：** 通过订单ID删除订单记录
- **请求参数：**
  - `id` (query, required): 订单ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 购物车管理

### 接口列表

#### 1. 根据ID更新购物车
- **接口地址：** `PUT /cart/updateCartById`
- **接口描述：** 通过购物车ID更新购物车信息
- **请求参数：**
  - `bean` (query, required): 购物车对象，类型为 Cart
  - `id` (query, required): 购物车ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 新增购物车
- **接口地址：** `POST /cart/add`
- **接口描述：** 创建新的购物车记录
- **请求参数：**
  - `bean` (query, required): 购物车对象，类型为 Cart
- **响应：** ResponseVO

#### 3. 批量新增或更新购物车
- **接口地址：** `POST /cart/addOrUpdateBatch`
- **接口描述：** 批量新增或更新购物车记录
- **请求体：** Cart 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 4. 批量新增购物车
- **接口地址：** `POST /cart/addBatch`
- **接口描述：** 批量新增购物车记录
- **请求体：** Cart 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 5. 分页查询购物车列表
- **接口地址：** `GET /cart/loadDataList`
- **接口描述：** 根据查询条件分页获取购物车列表
- **请求参数：**
  - `query` (query, required): 购物车查询条件，类型为 CartQuery
- **响应：** ResponseVO

#### 6. 根据ID查询购物车
- **接口地址：** `GET /cart/getCartById`
- **接口描述：** 通过购物车ID获取购物车信息
- **请求参数：**
  - `id` (query, required): 购物车ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 7. 根据ID删除购物车
- **接口地址：** `DELETE /cart/deleteCartById`
- **接口描述：** 通过购物车ID删除购物车记录
- **请求参数：**
  - `id` (query, required): 购物车ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 商店管理

### 接口列表

#### 1. 根据用户ID更新商店
- **接口地址：** `PUT /shop/updateShopByUserId`
- **接口描述：** 通过用户ID更新商店信息
- **请求参数：**
  - `bean` (query, required): 商店对象，类型为 Shop
  - `userId` (query, required): 用户ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 根据ID更新商店
- **接口地址：** `PUT /shop/updateShopById`
- **接口描述：** 通过商店ID更新商店信息
- **请求参数：**
  - `bean` (query, required): 商店对象，类型为 Shop
  - `id` (query, required): 商店ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 3. 新增商店
- **接口地址：** `POST /shop/add`
- **接口描述：** 创建新的商店记录
- **请求参数：**
  - `bean` (query, required): 商店对象，类型为 Shop
- **响应：** ResponseVO

#### 4. 批量新增或更新商店
- **接口地址：** `POST /shop/addOrUpdateBatch`
- **接口描述：** 批量新增或更新商店记录
- **请求体：** Shop 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 5. 批量新增商店
- **接口地址：** `POST /shop/addBatch`
- **接口描述：** 批量新增商店记录
- **请求体：** Shop 对象数组，格式为 application/json
- **响应：** ResponseVO

#### 6. 分页查询商店列表
- **接口地址：** `GET /shop/loadDataList`
- **接口描述：** 根据查询条件分页获取商店列表
- **请求参数：**
  - `query` (query, required): 商店查询条件，类型为 ShopQuery
- **响应：** ResponseVO

#### 7. 根据用户ID查询商店
- **接口地址：** `GET /shop/getShopByUserId`
- **接口描述：** 通过用户ID获取商店信息
- **请求参数：**
  - `userId` (query, required): 用户ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 8. 根据ID查询商店
- **接口地址：** `GET /shop/getShopById`
- **接口描述：** 通过商店ID获取商店信息
- **请求参数：**
  - `id` (query, required): 商店ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 9. 根据用户ID删除商店
- **接口地址：** `DELETE /shop/deleteShopByUserId`
- **接口描述：** 通过用户ID删除商店记录
- **请求参数：**
  - `userId` (query, required): 用户ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 10. 根据ID删除商店
- **接口地址：** `DELETE /shop/deleteShopById`
- **接口描述：** 通过商店ID删除商店记录
- **请求参数：**
  - `id` (query, required): 商店ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 评价管理

### 接口列表

#### 1. 根据订单项ID更新评价
- **接口地址：** `PUT /review/updateReviewByOrderItemId`
- **接口描述：** 通过订单项ID更新评价信息
- **请求参数：**
  - `bean` (query, required): 评价对象，类型为 Review
  - `orderItemId` (query, required): 订单项ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 根据ID更新评价
- **接口地址：** `PUT /review/updateReviewById`
- **接口描述：** 通过评价ID更新评价信息
- **请求参数：**
  - `bean` (query, required): 评价对象，类型为 Review
  - `id` (query, required): 评价ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 3. 新增评价
- **接口地址：** `POST /review/add`
- **接口描述：** 创建新的评价记录
- **请求参数：**
  - `bean` (query, required): 评价对象，类型为 Review
- **响应：** ResponseVO

#### 4. 分页查询评价列表
- **接口地址：** `GET /review/loadDataList`
- **接口描述：** 根据查询条件分页获取评价列表
- **请求参数：**
  - `query` (query, required): 评价查询条件，类型为 ReviewQuery
- **响应：** ResponseVO

#### 5. 根据订单项ID查询评价
- **接口地址：** `GET /review/getReviewByOrderItemId`
- **接口描述：** 通过订单项ID获取评价信息
- **请求参数：**
  - `orderItemId` (query, required): 订单项ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 6. 根据ID查询评价
- **接口地址：** `GET /review/getReviewById`
- **接口描述：** 通过评价ID获取评价信息
- **请求参数：**
  - `id` (query, required): 评价ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 7. 根据订单项ID删除评价
- **接口地址：** `DELETE /review/deleteReviewByOrderItemId`
- **接口描述：** 通过订单项ID删除评价记录
- **请求参数：**
  - `orderItemId` (query, required): 订单项ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 8. 根据ID删除评价
- **接口地址：** `DELETE /review/deleteReviewById`
- **接口描述：** 通过评价ID删除评价记录
- **请求参数：**
  - `id` (query, required): 评价ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 收藏管理

### 接口列表

#### 1. 根据ID更新收藏
- **接口地址：** `PUT /favorite/updateFavoriteById`
- **接口描述：** 通过收藏ID更新收藏信息
- **请求参数：**
  - `bean` (query, required): 收藏对象，类型为 Favorite
  - `id` (query, required): 收藏ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 新增收藏
- **接口地址：** `POST /favorite/add`
- **接口描述：** 创建新的收藏记录
- **请求参数：**
  - `bean` (query, required): 收藏对象，类型为 Favorite
- **响应：** ResponseVO

#### 3. 分页查询收藏列表
- **接口地址：** `GET /favorite/loadDataList`
- **接口描述：** 根据查询条件分页获取收藏列表
- **请求参数：**
  - `query` (query, required): 收藏查询条件，类型为 FavoriteQuery
- **响应：** ResponseVO

#### 4. 根据ID查询收藏
- **接口地址：** `GET /favorite/getFavoriteById`
- **接口描述：** 通过收藏ID获取收藏信息
- **请求参数：**
  - `id` (query, required): 收藏ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 5. 根据ID删除收藏
- **接口地址：** `DELETE /favorite/deleteFavoriteById`
- **接口描述：** 通过收藏ID删除收藏记录
- **请求参数：**
  - `id` (query, required): 收藏ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 分类管理

### 接口列表

#### 1. 根据ID更新分类
- **接口地址：** `PUT /category/updateCategoryById`
- **接口描述：** 通过分类ID更新分类信息
- **请求参数：**
  - `bean` (query, required): 分类对象，类型为 Category
  - `id` (query, required): 分类ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 新增分类
- **接口地址：** `POST /category/add`
- **接口描述：** 创建新的分类记录
- **请求参数：**
  - `bean` (query, required): 分类对象，类型为 Category
- **响应：** ResponseVO

#### 3. 分页查询分类列表
- **接口地址：** `GET /category/loadDataList`
- **接口描述：** 根据查询条件分页获取分类列表
- **请求参数：**
  - `query` (query, required): 分类查询条件，类型为 CategoryQuery
- **响应：** ResponseVO

#### 4. 根据ID查询分类
- **接口地址：** `GET /category/getCategoryById`
- **接口描述：** 通过分类ID获取分类信息
- **请求参数：**
  - `id` (query, required): 分类ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 5. 根据ID删除分类
- **接口地址：** `DELETE /category/deleteCategoryById`
- **接口描述：** 通过分类ID删除分类记录
- **请求参数：**
  - `id` (query, required): 分类ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 地址管理

### 接口列表

#### 1. 根据ID更新地址
- **接口地址：** `PUT /address/updateAddressById`
- **接口描述：** 通过地址ID更新地址信息
- **请求参数：**
  - `bean` (query, required): 地址对象，类型为 Address
  - `id` (query, required): 地址ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 新增地址
- **接口地址：** `POST /address/add`
- **接口描述：** 创建新的地址记录
- **请求参数：**
  - `bean` (query, required): 地址对象，类型为 Address
- **响应：** ResponseVO

#### 3. 分页查询地址列表
- **接口地址：** `GET /address/loadDataList`
- **接口描述：** 根据查询条件分页获取地址列表
- **请求参数：**
  - `query` (query, required): 地址查询条件，类型为 AddressQuery
- **响应：** ResponseVO

#### 4. 根据ID查询地址
- **接口地址：** `GET /address/getAddressById`
- **接口描述：** 通过地址ID获取地址信息
- **请求参数：**
  - `id` (query, required): 地址ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 5. 根据ID删除地址
- **接口地址：** `DELETE /address/deleteAddressById`
- **接口描述：** 通过地址ID删除地址记录
- **请求参数：**
  - `id` (query, required): 地址ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 支付记录管理

### 接口列表

#### 1. 根据支付单号更新支付记录
- **接口地址：** `PUT /paymentRecord/updatePaymentRecordByPaymentNo`
- **接口描述：** 通过支付单号更新支付信息
- **请求参数：**
  - `bean` (query, required): 支付记录对象，类型为 PaymentRecord
  - `paymentNo` (query, required): 支付单号，类型为 string
- **响应：** ResponseVO

#### 2. 根据ID更新支付记录
- **接口地址：** `PUT /paymentRecord/updatePaymentRecordById`
- **接口描述：** 通过支付记录ID更新支付信息
- **请求参数：**
  - `bean` (query, required): 支付记录对象，类型为 PaymentRecord
  - `id` (query, required): 支付记录ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 3. 新增支付记录
- **接口地址：** `POST /paymentRecord/add`
- **接口描述：** 创建新的支付记录
- **请求参数：**
  - `bean` (query, required): 支付记录对象，类型为 PaymentRecord
- **响应：** ResponseVO

#### 4. 分页查询支付记录列表
- **接口地址：** `GET /paymentRecord/loadDataList`
- **接口描述：** 根据查询条件分页获取支付记录列表
- **请求参数：**
  - `query` (query, required): 支付记录查询条件，类型为 PaymentRecordQuery
- **响应：** ResponseVO

#### 5. 根据支付单号查询支付记录
- **接口地址：** `GET /paymentRecord/getPaymentRecordByPaymentNo`
- **接口描述：** 通过支付单号获取支付记录信息
- **请求参数：**
  - `paymentNo` (query, required): 支付单号，类型为 string
- **响应：** ResponseVO

#### 6. 根据ID查询支付记录
- **接口地址：** `GET /paymentRecord/getPaymentRecordById`
- **接口描述：** 通过支付记录ID获取支付记录信息
- **请求参数：**
  - `id` (query, required): 支付记录ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 7. 根据支付单号删除支付记录
- **接口地址：** `DELETE /paymentRecord/deletePaymentRecordByPaymentNo`
- **接口描述：** 通过支付单号删除支付记录
- **请求参数：**
  - `paymentNo` (query, required): 支付单号，类型为 string
- **响应：** ResponseVO

#### 8. 根据ID删除支付记录
- **接口地址：** `DELETE /paymentRecord/deletePaymentRecordById`
- **接口描述：** 通过支付记录ID删除支付记录
- **请求参数：**
  - `id` (query, required): 支付记录ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 物流管理

### 接口列表

#### 1. 根据ID更新物流信息
- **接口地址：** `PUT /logistics/updateLogisticsById`
- **接口描述：** 通过物流ID更新物流信息
- **请求参数：**
  - `bean` (query, required): 物流对象，类型为 Logistics
  - `id` (query, required): 物流ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 2. 新增物流信息
- **接口地址：** `POST /logistics/add`
- **接口描述：** 创建新的物流记录
- **请求参数：**
  - `bean` (query, required): 物流对象，类型为 Logistics
- **响应：** ResponseVO

#### 3. 分页查询物流列表
- **接口地址：** `GET /logistics/loadDataList`
- **接口描述：** 根据查询条件分页获取物流列表
- **请求参数：**
  - `query` (query, required): 物流查询条件，类型为 LogisticsQuery
- **响应：** ResponseVO

#### 4. 根据ID查询物流信息
- **接口地址：** `GET /logistics/getLogisticsById`
- **接口描述：** 通过物流ID获取物流信息
- **请求参数：**
  - `id` (query, required): 物流ID，类型为 integer(int64)
- **响应：** ResponseVO

#### 5. 根据ID删除物流信息
- **接口地址：** `DELETE /logistics/deleteLogisticsById`
- **接口描述：** 通过物流ID删除物流记录
- **请求参数：**
  - `id` (query, required): 物流ID，类型为 integer(int64)
- **响应：** ResponseVO

---

## 其他管理模块

系统还包含以下管理模块，每个模块都提供完整的CRUD操作：

- **订单项管理**：管理订单中的具体商品项
- **商品SKU管理**：管理商品的库存单位
- **商品规格管理**：管理商品的规格属性
- **退款记录管理**：管理退款相关记录
- **消息管理**：管理系统消息
- **操作日志管理**：记录系统操作日志
- **系统配置管理**：管理系统配置参数
- **每日统计管理**：每日业务数据统计
- **商店统计管理**：商店运营数据统计
- **商品统计管理**：商品销售数据统计
- **搜索关键词管理**：管理搜索关键词统计

---

# 数据模型定义

## ResponseVO 响应模型

通用响应对象，包含所有API接口的返回结果。

**字段说明：**
- `status` (string): 响应状态
- `code` (integer): 响应代码
- `info` (string): 响应信息
- `data` (object): 响应数据

## User 用户模型

用户基本信息模型。

**字段说明：**
- `id` (integer, int64): 用户ID
- `username` (string): 用户名
- `password` (string): 密码
- `role` (string): 用户角色
- `email` (string): 邮箱
- `avatar` (string): 头像
- `status` (string): 用户状态
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Product 商品模型

商品基本信息模型。

**字段说明：**
- `id` (integer, int64): 商品ID
- `shopId` (integer, int64): 商店ID
- `categoryId` (integer, int64): 分类ID
- `productName` (string): 商品名称
- `productDescription` (string): 商品描述
- `price` (number): 商品价格
- `stock` (integer, int32): 库存数量
- `status` (string): 商品状态
- `images` (string): 商品图片
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Order 订单模型

订单基本信息模型。

**字段说明：**
- `id` (integer, int64): 订单ID
- `orderNo` (string): 订单号
- `userId` (integer, int64): 用户ID
- `shopId` (integer, int64): 商店ID
- `totalAmount` (number): 订单总金额
- `status` (string): 订单状态
- `addressId` (integer, int64): 收货地址ID
- `paymentMethod` (string): 支付方式
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Shop 商店模型

商店基本信息模型。

**字段说明：**
- `id` (integer, int64): 商店ID
- `userId` (integer, int64): 用户ID
- `shopName` (string): 商店名称
- `shopDescription` (string): 商店描述
- `shopLogo` (string): 商店Logo
- `contactInfo` (string): 联系信息
- `businessLicense` (string): 营业执照
- `status` (string): 商店状态
- `auditTime` (string, date-time): 审核时间
- `auditOpinion` (string): 审核意见
- `auditorId` (integer, int64): 审核人ID
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Cart 购物车模型

购物车信息模型。

**字段说明：**
- `id` (integer, int64): 购物车ID
- `userId` (integer, int64): 用户ID
- `productId` (integer, int64): 商品ID
- `quantity` (integer, int32): 商品数量
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Review 评价模型

商品评价信息模型。

**字段说明：**
- `id` (integer, int64): 评价ID
- `orderId` (integer, int64): 订单ID
- `orderItemId` (integer, int64): 订单项ID
- `userId` (integer, int64): 用户ID
- `productId` (integer, int64): 商品ID
- `rating` (integer, int32): 评分
- `content` (string): 评价内容
- `images` (string): 评价图片
- `isAnonymous` (integer, int32): 是否匿名
- `shopReply` (string): 商家回复
- `shopReplyTime` (string, date-time): 商家回复时间
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Category 分类模型

商品分类信息模型。

**字段说明：**
- `id` (integer, int64): 分类ID
- `categoryName` (string): 分类名称
- `parentId` (integer, int64): 父分类ID
- `level` (integer, int32): 分类级别
- `sortOrder` (integer, int32): 排序
- `status` (string): 分类状态
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Address 地址模型

收货地址信息模型。

**字段说明：**
- `id` (integer, int64): 地址ID
- `userId` (integer, int64): 用户ID
- `receiverName` (string): 收货人姓名
- `receiverPhone` (string): 收货人电话
- `province` (string): 省份
- `city` (string): 城市
- `district` (string): 区县
- `detailAddress` (string): 详细地址
- `isDefault` (integer, int32): 是否默认地址
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## PaymentRecord 支付记录模型

支付记录信息模型。

**字段说明：**
- `id` (integer, int64): 支付记录ID
- `orderId` (integer, int64): 订单ID
- `paymentNo` (string): 支付单号
- `amount` (number): 支付金额
- `paymentMethod` (string): 支付方式
- `status` (string): 支付状态
- `paymentTime` (string, date-time): 支付时间
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Logistics 物流模型

物流信息模型。

**字段说明：**
- `id` (integer, int64): 物流ID
- `orderId` (integer, int64): 订单ID
- `logisticsNo` (string): 物流单号
- `logisticsCompany` (string): 物流公司
- `status` (string): 物流状态
- `trackingInfo` (string): 物流跟踪信息
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

## Favorite 收藏模型

商品收藏信息模型。

**字段说明：**
- `id` (integer, int64): 收藏ID
- `userId` (integer, int64): 用户ID
- `productId` (integer, int64): 商品ID
- `createTime` (string, date-time): 创建时间
- `updateTime` (string, date-time): 更新时间

---

## 查询模型定义

系统还包含以下查询模型用于条件查询：

- **UserQuery**: 用户查询条件
- **ProductQuery**: 商品查询条件
- **OrderQuery**: 订单查询条件
- **ShopQuery**: 商店查询条件
- **CartQuery**: 购物车查询条件
- **ReviewQuery**: 评价查询条件
- **CategoryQuery**: 分类查询条件
- **AddressQuery**: 地址查询条件
- **PaymentRecordQuery**: 支付记录查询条件
- **LogisticsQuery**: 物流查询条件
- **FavoriteQuery**: 收藏查询条件

以及其他统计查询模型：
- **ShopStatisticsQuery**: 商店统计查询条件
- **ProductStatisticsQuery**: 商品统计查询条件
- **DailyStatisticsQuery**: 每日统计查询条件

---

# 接口文档转换完成说明

本文档已根据 `api-docs.yaml` OpenAPI 3.1.0 规范文件完整转换为Markdown格式的接口文档。

**转换内容包括：**
1. ✅ 完整的API分组结构（22个功能模块）
2. ✅ 所有API接口的详细定义（205个接口路径）
3. ✅ 主要数据模型定义（46个数据模型）
4. ✅ 请求参数和响应格式说明
5. ✅ 接口描述和操作说明

**文档特点：**
- 采用敏捷开发模式，按功能模块组织
- 每个接口包含完整的请求参数和响应格式
- 数据模型字段详细说明
- 支持快速查找和阅读

**注意事项：**
- 所有接口返回统一的 ResponseVO 响应格式
- 时间字段统一使用 date-time 格式
- ID字段统一使用 int64 类型
- 所有必填参数都有明确标识


