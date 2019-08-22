class GlobalVal:
    test_id=0 #测试编号
    test_name =1 #测试名称
    request_url = 2 #请求地址
    request_method = 3 #请求方法 post get
    request_header =4 #请求头
    request_data =5 #请求数据
    is_test =6 #是否测试
    expected_res = 7 #预期结果
    actual_res = 8  #实际结果
    test_res = 9 #测试结果

def getTestIdcol():
    """
    获取测试编号的列数
    :return:
    """
    return GlobalVal.test_id

def getTestNamecol():
    """
    获取测试名称的列
    :return:
    """
    return GlobalVal.test_name

def getRequestUrlcol():
    """
    获取请求地址的列数
    :return:
    """
    return GlobalVal.request_url

def getRequestMethodcol():
    """
    获取请求方法的列数
    :return:
    """
    return GlobalVal.request_method

def getRequestHeadercol():
    """
    获取请求头的列数
    :return:
    """
    return GlobalVal.request_header

def getRequestDatacol():
    """
    获取请求数据的列数
    :return:
    """
    return GlobalVal.request_data

def getIsTestcol():
    """
    是否测试的列数
    :return:
    """
    return GlobalVal.is_test

def getExpectedResultcol():
    """
    获取预期结果的列数
    :return:
    """
    return GlobalVal.expected_res

def getActualResultcol():
    """
    获取实际结果的列数
    :return:
    """
    return GlobalVal.actual_res

def getTestResultcol():
    """
    测试结果的列
    :return:
    """
    return GlobalVal.test_res

headers={"Host": "m.imooc.com",
"Connection": "keep-alive",
"Content-Length": "277",
"Accept": "application/json, text/javascript, */*; q=0.01",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
"Sec-Fetch-Mode": "cors",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Origin": "https://m.imooc.com",
"Sec-Fetch-Site": "same-origin",
"Cookie": "imooc_uuid=36c7b2c2-78d0-41b1-9378-a7847a85f272; imooc_isnew_ct=1565919021; zg_did=%7B%22did%22%3A%20%2216c980c0be4413-0730b11462efab-7373e61-144000-16c980c0be6969%22%7D; imooc_isnew=2; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1565919022,1566018930; IMCDNS=0; cvde=5d5e2dffa2c4c-2; Hm_lvt_c92536284537e1806a07ef3e6873f2b3=1566457168; PHPSESSID=hhl7k5ucrguojto846f7f70fn3; UM_distinctid=16cb81f9c342b2-0fa39518e3dacd-7373e61-144000-16cb81f9c35160; CNZZDATA1261728817=185315549-1566454520-https%253A%252F%252Fm.imooc.com%252F%7C1566459931; Hm_lpvt_c92536284537e1806a07ef3e6873f2b3=1566460244; zg_f375fe2f71e542a4b890d9a620f9fb32=%7B%22sid%22%3A%201566457168158%2C%22updated%22%3A%201566460246831%2C%22info%22%3A%201565919022062%2C%22superProperty%22%3A%20%22%7B%5C%22Platform%5C%22%3A%20%5C%22wap%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22m.imooc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201566457168158%7D",
"Referer": "https://m.imooc.com/account/otherlogin?backurl=https://m.imooc.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"}
