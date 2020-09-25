
from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''




def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers ={}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data='''{
  "pwd": "jhihu1234",
  "userName": "x0B3UUhQZM"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_addProd(pub_data):
    pub_data["price"] = "自动生成  数字 20,8000"
    pub_data["prc"] = "自动生成 字符串 4 数字 ibnh"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "创建产品成功"  # 预期结果
    json_data='''{
  "brand": "None",
  "colors": ["白色","红色"],
  "price": "${price}",
  "productCode": "${prc}",
  "productName": "小米手机",
  "sizes": ["3寸"],
  "type": "数码"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"sku": "$['data'][0]['skuCode']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)



def test_getSKU(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'SKU': '${sku}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)



def test_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'SKU': '${sku}', 'price': '1000'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)




def test_changePriceByProdCode(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '批量修改价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "更新成功"  # 预期结果
    data={'price': '5000', 'prodCode': '${prc}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)






