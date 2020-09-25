import allure
import requests
#requests发送http请求

@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名1")
def test_no_params():
    #使用requests.get发送一个get请求。
    r = requests.get("https://www.baidu.com/")
    #使用requests.request发送一个get请求。
    r = requests.request(method="GET",url="http://www.baidu.com/")
    sess = requests.session() #使用session建立连接
    print(sess.headers)
    r = sess.request(method="GET",url="http://www.baidu.com/")#再发送请求，无论请求多少次，连接只建立
    r = sess.request(method="GET", url="http://www.baidu.com/")
    print(r.text)#test获取响应对象中。响应正文的数据


@allure.feature("get请求")
@allure.story("有参数")
@allure.title("用例名2")
def test_get_params():
    with allure.step("第一步、准备测试数据"):pass
    pa = {"accountName":"xuepl123"}
    with allure.step("第二步、发送请求")：pass
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params=pa)
    with allure.step("第三步、请求数据“)：
        allure.attach("请求行，请求头,请求正文","请求信息"，allure.attachment_type.TEXT)
    print(r.text)
    with open()


@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名3")
def test_get_path():
    r=requests.request("GET","http://qa.yansl.com/:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1, pageSize=1))
    print(r.text)


@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名4")
def test_get_file(pub_data):
    p = {"pridCode":"63803y"}
    h = {"token":pub_data["token"]}
    r = requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with open("aa.xls","wb")as f:
        f.write(r.content)




@allure.feature("post请求")
@allure.story("有参数")
@allure.title("用例名5")
def test_post_json():
    data ={
    "pwd":"abc123",
    "userName":"tuu653"
    }
    r = requests.post("http://qa.yansl.com:8084/login",json=data)
    print(r.text)


@allure.feature("post请求")
@allure.story("有参数")
@allure.title("用例名6")
def test_post_formdata(pub_data):
    data = {
    "userNanme":"tan242743"
    }
    h = {"token":pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/user/lock",data=data,headers=h)
    print((r.text))


@allure.feature("post请求")
@allure.story("有参数")
@allure.title("用例名6")
def test_post_upload_file(pub_data):
    data  = {
        "file":open("aa.xls","rb")
    }
    h = {"token":pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory",files=data,headers=h)
    print(r.text)


