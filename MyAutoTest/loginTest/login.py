import requests
from TestMain.utils import Utils
from TestMain.mockData import Mock
import threading
import datetime
from queue import Queue

add_user_queue = Queue()  # 添加用户信息队列
login_header_queue = Queue()  # 登录请求头队列
check_response_queue = Queue()  # 检测response队列
del_user_queue = Queue()  # 删除用户队列
init_user_id = 100000  # 用户起始id
init_user_pwd = "123456"  # 用户数据默认密码
functionalRoleList = ""  # 用户默认角色列表
resourceRoleList = ""  # 用户默认资源列表
content_lenght = "123"  # 默认添加用户数据字段长度
thread_num = 200  # 默认开启线程数
add_user_num = 100  # 默认添加用户数
login_user_num = 100  # 默认登录用户数
mock = Mock()
utils = Utils()
login_name = "admin"  # 登录用户名
login_pwd = "123456"  # 登录密码
login_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin"  # 登录接口
add_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser"  # 添加用户接口
del_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserDeleteUser"  # 删除用户接口
add_user_data = '{"accountInfo":{"userID":"%s","username":"%s","password":"123456","functionalRoleList":"",' \
                '"resourceRoleList":""}} '

add_user_data2 = {"accountInfo":
                      {"userID": "",
                       "username": "",
                       "password": init_user_pwd,
                       "functionalRoleList": functionalRoleList,
                       "resourceRoleList": resourceRoleList}
                  }

login_headers = utils.encapsulate_headers(login_name, login_pwd)

add_user_header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Auth-Token': "",
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': "",
    'Content-Type': 'application/json',
    'Host': '10.0.20.126',
    'Referer': 'http://10.0.20.126/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

del_user_header = add_user_header  # 删除用户请求头

response_headers = requests.post(url=login_url, headers=login_headers).headers
# response_headers = mock.main(method="post", url=login_url, headers=login_headers)

print(response_headers)

add_user_header['Auth-Token'] = response_headers["auth-token"]  # 登录获取authtoken


def check_res():
    while not check_response_queue.empty():
        response = check_response_queue.get()
        if response['returnState']['stateCode'] == 0:
            print("success")
        else:
            print("response error", response['returnState']['stateCode'])


def generate_user_info(user_id, max_num=100):
    """
    生成用户信息
    :param user_id: 起始用户id
    :param max_num: 生成用户个数
    :return:
    """
    global add_user_queue, login_header_queue
    for i in range(max_num):
        user_info = add_user_data % (user_id + i, "li" + str(user_id + i))

        # add_user_data2["accountInfo"]["userID"] = str(user_id + i)
        # add_user_data2["accountInfo"]["username"] = "li" + str(user_id + i)
        # user_info = add_user_data2

        add_user_queue.put(user_info)
        login_header_queue.put(utils.encapsulate_headers(name=str(user_id + i), password=str(user_id + i)))
        del_user_queue.put(user_id + i)


def add_user():
    global add_user_queue
    while not add_user_queue.empty():
        user_data = add_user_queue.get(timeout=3)
        response = requests.post(url=add_user_url, data=user_data, headers=add_user_header)
        check_response_queue.put(response.json())


def user_login():
    global login_header_queue
    while not login_header_queue.empty():
        headers = login_header_queue.get()
        # response = mock.main(method="post", url=login_url, headers=headers)
        response = requests.post(url=login_url, headers=login_headers)
        check_response_queue.put(response.json())


def del_user():
    global del_user_queue
    while not del_user_queue.empty():
        user_id = del_user_queue.get()
        response = requests.post(url=del_user_url, data='{"userID": "%s"}' % str(user_id), headers=add_user_header)
        check_response_queue.put(response.json())


if __name__ == "__main__":

    # 添加用户
    print("添加用户中")
    generate_user_info(init_user_id, add_user_num)
    add_user_thread_list = []
    for i in range(thread_num):
        add_user_thread = threading.Thread(target=add_user, args=())
        add_user_thread_list.append(add_user_thread)

    for one in add_user_thread_list:
        one.start()

    for one in add_user_thread_list:
        one.join()

    check_res_thread_list = []
    for i in range(thread_num):
        check_res_thread = threading.Thread(target=check_res, args=())
        check_res_thread_list.append(check_res_thread)

    for one in check_res_thread_list:
        one.start()

    for one in check_res_thread_list:
        one.join()

    print("添加完成")

    # 登录测试

    print("开始登录测试")
    user_login_thread_list = []
    start = datetime.datetime.now()
    for i in range(thread_num):
        user_login_thread = threading.Thread(target=user_login, args=())
        user_login_thread_list.append(user_login_thread)

    for one in user_login_thread_list:
        one.start()

    for one in user_login_thread_list:
        one.join()

    check_res_thread_list = []
    for i in range(thread_num):
        check_res_thread = threading.Thread(target=check_res, args=())
        check_res_thread_list.append(check_res_thread)

    for one in check_res_thread_list:
        one.start()

    for one in check_res_thread_list:
        one.join()

    end = datetime.datetime.now()
    print("time", end - start)

    # 删除用户

    print("开始删除测试")
    user_del_thread_list = []
    for i in range(thread_num):
        user_del_thread = threading.Thread(target=del_user, args=())
        user_del_thread_list.append(user_del_thread)

    for one in user_del_thread_list:
        one.start()

    for one in user_del_thread_list:
        one.join()

    check_res_thread_list = []
    for i in range(thread_num):
        check_res_thread = threading.Thread(target=check_res, args=())
        check_res_thread_list.append(check_res_thread)

    for one in check_res_thread_list:
        one.start()

    for one in check_res_thread_list:
        one.join()

    end = datetime.datetime.now()
    print("time", end - start)
