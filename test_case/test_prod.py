from tools.api import request_tool
# json path，参数类型为列表 根据jsonpath提取响应正文中的数据
from tools.security.md5_tool import md5_passwd


def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data ='''
    {
        "brand": "匡威",
        "colors": [
            "红"
        ],
        "price": 499,
        "productCode": "自动生成 字符串 5 数字字母",
        "productName": "匡威123",
        "sizes": [
            "38","39"
        ],
        "type": "鞋子"
    }
    '''
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]



def test_change_price(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":pub_data["skuCode"],"price":499}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]

from tools.api import request_tool

def test_post_product(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '增量库存'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":'pub_data["productCode"]',"qty":"100"}
    headers = {"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]

def test_post_order(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '无签名无加密下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
	"ordeerPrice": 599,
	"orderLineList": [{
		"qty": 1,
		"skuCode": "pub_data["skuCode"]"
	}],
	"receiver": "小仙女",
	"receiverPhone": "17717777777",
	"receivingAddress": "上海市闸北区",
	"sign": "小仙女",
	"userName": "xxn777"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]


'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_post_SignBody(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '数字签名下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    headers = {"token":pub_data["token"]}
    s = "receiver=xxn777&ordeerPrice=599&receiverPhone=17717777777&key=guoya"
    sign=md5_passwd("s","")
    pub_data["sign"]=sign
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
	"ordeerPrice": 599,
	"orderLineList": [{
		"qty": 1,
		"skuCode": "pub_data["skuCode"]"
	}],
	"receiver": "小仙女",
	"receiverPhone": "17717777777",
	"receivingAddress": "上海市闸北区",
	"sign": "${sign}",
	"userName": "xxn777"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]



# def test_post_json(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "产品模块"  # allure报告中一级分类
#     story = '增加产品'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/addProd"  # 接口地址
#     headers = {"token":pub_data["token"]}
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "brand": "耐克",
#   "colors": [
#     "牛油果绿","静谧深灰","彩虹ranbiow"
#   ],
#   "price": 599,
#   "productCode": "NK2",
#   "productName": "耐克2",
#   "sizes": [
#     "37","38","39"
#   ],
#   "type": "服装"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r=request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
#     pub_data["skuCode"]=r.json()["data"][0]["skuCode"]
#
# def test_post_data(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "产品模块"  # allure报告中一级分类
#     story = '修改价格'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePrice"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     data = {"SKU":'skuCode',"price":499}
#     headers={"token":pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
