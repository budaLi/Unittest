class GlobalVal:
    test_id=0 #测试编号
    test_name =1 #测试名称
    request_url = 2 #请求地址
    request_method = 3 #请求方法 post get
    request_header =4 #请求头
    depend_id = 5      #依赖ID
    depend_data = 6     #依赖数据
    depend_data_belong = 7    #依赖数据所属字段
    request_data =8 #请求数据
    note = 9   #备注
    is_test =10 #是否测试
    expected_res = 11 #预期结果
    actual_res = 12  #实际结果
    test_res = 13 #测试结果

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

def getDepenIdcol():
    """
    返回依赖id所在列
    :return:
    """
    return GlobalVal.depend_id

def getDependDatacol():
    """
    依赖数据所在列
    :return:
    """
    return GlobalVal.depend_data

def getDependDataBelongcol():
    """
    依赖数据所属字段所在列
    :return:
    """
    return GlobalVal.depend_data_belong

def getRequestDatacol():
    """
    获取请求数据的列数
    :return:
    """
    return GlobalVal.request_data

def getNotecol():
    """
    备注所在列
    :return:
    """
    return GlobalVal.note

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

headers={
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-CN',
   'Authorization': 'Basic YWRtaW46MTIzNDU2', # admin:123456
   'Cache-Control': 'no-cache',
   'Connection': 'Keep-Alive',
   'Content-Length': '0',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Host': '10.0.20.126',
   'Referer': 'http://10.0.20.126/',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

headers2={
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate',
    'Auth-Token': '1568137083',
   'Accept-Language': 'zh-CN',
   'Connection': 'keep-alive',
   'Content-Length': '0',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Host': '10.0.20.126',
   'Referer': 'http://10.0.20.126/',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

s='{"accountInfo":{"userID":"100000","username":"libuda","password":"123456","functionalRoleList":"","resourceRoleList":""}}'
print(len(s))

