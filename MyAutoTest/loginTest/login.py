# 登录获取authtoken
import requests
from TestMain.utils import Utils
from TestMain.mockData import Mock
import threading


mock = Mock()
utils = Utils()
login_name = "admin"
login_pwd = "123456"
login_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin"
add_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser"
add_user_data = '{"accountInfo":{"userID":"%s","username":"%s","password":"123456","functionalRoleList":"",' \
                '"resourceRoleList":""}} '

login_headers = utils.encapsulate_headers(login_name, login_pwd)

add_user_header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Auth-Token': "",
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': "",
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '10.0.20.126',
    'Referer': 'http://10.0.20.126/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

# response_headers = requests.post(url=login_url, headers=login_headers).headers
response_headers = mock.main(method="post",url=login_url, headers=login_headers)

print(response_headers)

# add_user_header['Auth-Token'] = response_headers["auth-token"]


def chack_res(response):
    response = eval(response)
    return response['returnState']['stateCode'] == 0


def add_user(user_data):
    response = mock.main(method="post", url=add_user_url, data=user_data, headers=add_user_header)
    if chack_res(response):
        print("添加用户成功 %s"%user_data)


# def add_user2(add_user_num):
#     add_user_success = 0
#     username_prefix = "mm"
#     user_id_pre = 10000
#
#     while add_user_success <= add_user_num:
#         user_id = str(user_id_pre)
#         username = username_prefix + user_id
#         add_use = add_user_data%(user_id, username)
#         # response = requests.post(url=add_user_url, data=add_use, headers=add_user_header).json()
#
#         response = mock.main(method="post",url=add_user_url, data=add_use, headers=add_user_header)
#         if chack_res(response):
#             print("添加用户%s成功"%user_id)
#             add_user_success += 1
#         user_id_pre += 1
#     print("添加用户完毕")


if __name__=="__main__":
    # add_user(10000)
    import datetime
    start = datetime.datetime.now()
    the = []
    for i in range(1000):
        user1 = str(i)
        the.append(threading.Thread(target=add_user,args=(user1,)))
    count = 0
    for one in the:
        one.start()
    end = datetime.datetime.now()
    print("time",end-start)
