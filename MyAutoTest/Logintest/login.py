import requests
import base64
import threading
import datetime
from queue import Queue


class Utils:
    
    def encrypt_by_base64(self, strs):
        """
        对字符串进行base64加密
        :param strs:
        :return:
        """
        # 编码与解码的处理对象是byte，故对原数据要先编码，使原本的str类型变成byte，解码后直接输出来的是byte对象，故要解码成str对象。
        strs = base64.b64encode(strs.encode())
        res = strs.decode()
        return res

    def encapsulate_headers(self, name, password):
        """
        对密码及headers进行封装
        :return:
        """
        if isinstance(password, float):
            password = int(password)
        tem = str(name) + ":" + str(password)
        strs = self.encrypt_by_base64(tem)
        headers = {
            'Authorization': 'Basic ' + strs,  # admin:123456
        }
        return headers


# 20.0.88.xxx  255.255.0.0
class LoginTest:
    def __init__(self):
        self.init_proxy_ip = "http://20.0.88.%s:80"  # 初始ip
        self.max_use = 50  # 每个ip最大使用次数
        self.proxy_pools = self.gen_proxy_pool(num=20)  # 代理ip  num  生成ip个数
        self.add_user_queue = Queue()  # 添加用户信息队列
        self.login_header_queue = Queue()  # 登录请求头队列
        self.check_response_queue = Queue()  # 检测response队列
        self.del_user_queue = Queue()  # 删除用户队列
        self.init_user_id = 100000  # 用户起始id
        self.init_user_pwd = "123456"  # 用户数据默认密码
        self.functionalRoleList = ""  # 用户默认角色列表
        self.resourceRoleList = ""  # 用户默认资源列表
        self.content_length = "123"  # 默认添加用户数据字段长度
        self.add_user_num = 100  # 默认添加用户数
        self.login_user_num = self.add_user_num  # 默认登录用户数
        self.thread_num = int(self.add_user_num / 10) if self.add_user_num < 100 else int(
            self.add_user_num / 100)  # 默认开启线程数
        self.user_name_prefix = "li"
        self.utils = Utils()
        self.login_name = "admin"  # 登录用户名
        self.login_pwd = "123456"  # 登录密码
        self.login_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin"  # 登录接口
        self.add_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser"  # 添加用户接口
        self.del_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserDeleteUser"  # 删除用户接口
        self.add_user_data = '{"accountInfo":{"userID":"%s","username":"%s","password":"123456",' \
                             '"functionalRoleList":"",' \
                             '"resourceRoleList":""}} '

        self.add_user_data2 = {"accountInfo":
                                   {"userID": "",
                                    "username": "",
                                    "password": self.init_user_pwd,
                                    "functionalRoleList": self.functionalRoleList,
                                    "resourceRoleList": self.resourceRoleList}
                               }

        self.login_headers = self.utils.encapsulate_headers(self.login_name, self.login_pwd)

        self.init_add_user_header = {
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
        self.add_user_header = self.get_add_user_headers()
        self.del_user_header = self.add_user_header  # 删除用户请求头

    def get_add_user_headers(self):
        """
        模拟登录获取authtoken
        :return:
        """
        response_headers = requests.post(url=self.login_url, headers=self.login_headers).headers

        self.init_add_user_header['Auth-Token'] = response_headers["auth-token"]  # 登录获取authtoken
        return self.init_add_user_header

    def gen_proxy_pool(self, num):
        """
        ip代理池
        :param num:  代理ip数量
        :return:
        """
        proxy_pools_queue = Queue()
        for i in range(num):
            for _ in range(self.max_use):
                proxy_pools_queue.put(self.init_proxy_ip % str(i))
        return proxy_pools_queue

    def check_res(self):
        """
        状态检测
        :return:
        """
        success = 0
        fail = 0
        while not self.check_response_queue.empty():
            response = self.check_response_queue.get()
            if response['returnState']['stateCode'] == 0:
                success += 1
            else:
                fail += 1
                print("response error", response['returnState']['stateCode'])
        print("success : %s  fail :%s" % (success, fail))

    def generate_user_info(self, user_id, max_num=100):
        """
        生成用户信息
        :param user_id: 起始用户id
        :param max_num: 生成用户个数
        :return:
        """
        for i in range(max_num):
            user_info = self.add_user_data % (user_id + i, self.user_name_prefix + str(user_id + i))
            # add_user_data2["accountInfo"]["userID"] = str(user_id + i)
            # add_user_data2["accountInfo"]["username"] = "li" + str(user_id + i)
            # user_info = add_user_data2
            self.add_user_queue.put(user_info)
            tem = self.utils.encapsulate_headers(name=self.user_name_prefix + str(user_id + i),
                                                 password=self.init_user_pwd)
            self.login_header_queue.put(tem)
            self.del_user_queue.put(user_id + i)

    def add_user(self):
        """
        添加用户
        :return:
        """
        while not self.add_user_queue.empty():
            user_data = self.add_user_queue.get(timeout=3)
            response = requests.post(url=self.add_user_url, data=user_data, headers=self.add_user_header)
            self.check_response_queue.put(response.json())

    def user_login(self):
        """
        用户登录
        :return:
        """
        proxies = ""

        while not self.login_header_queue.empty():
            headers = self.login_header_queue.get()
            if not self.proxy_pools.empty():
                proxies = self.proxy_pools.get()
            proxy_dict = {
                'http': proxies,  # 注意此处是http的ip
            }
            try:
                response = requests.post(url=self.login_url, headers=headers, proxies=proxy_dict)
                print(response)
            except Exception as e:
                print(e)
                response = requests.post(url=self.login_url, headers=headers)
                self.check_response_queue.put(response.json())

    def del_user(self):
        """
        删除用户
        :return:
        """
        while not self.del_user_queue.empty():
            user_id = self.del_user_queue.get()
            response = requests.post(url=self.del_user_url, data='{"userID": "%s"}' % str(user_id),
                                     headers=self.add_user_header)
            self.check_response_queue.put(response.json())

    def main(self):
        key = input("是否添加用户 y/n")
        # 添加用户
        if key == "y":
            print("添加用户中")
            self.generate_user_info(self.init_user_id, self.add_user_num)
            add_user_thread_list = []
            for i in range(self.thread_num):
                add_user_thread = threading.Thread(target=self.add_user, args=())
                add_user_thread_list.append(add_user_thread)

            for one in add_user_thread_list:
                one.start()
            for one in add_user_thread_list:
                one.join()

            print("添加完成")

            key = input("是否进行登录测试 y/n")
            if key == "y":
                # 登录测试
                print("开始登录测试")
                user_login_thread_list = []
                start = datetime.datetime.now()
                for i in range(self.thread_num):
                    user_login_thread = threading.Thread(target=self.user_login, args=())
                    user_login_thread_list.append(user_login_thread)

                for one in user_login_thread_list:
                    one.start()
                for one in user_login_thread_list:
                    one.join()

                end = datetime.datetime.now()
                print("time", end - start)

                print("登录测试完成")

            key = input("是否进行删除测试 y/n")
            if key == "y":
                # 删除用户
                print("开始删除测试")
                user_del_thread_list = []
                for i in range(self.thread_num):
                    user_del_thread = threading.Thread(target=self.del_user, args=())
                    user_del_thread_list.append(user_del_thread)

                for one in user_del_thread_list:
                    one.start()
                for one in user_del_thread_list:
                    one.join()
                print("删除测试完成")

                # 状态检测
                check_res_thread_list = []
                for i in range(self.thread_num):
                    check_res_thread = threading.Thread(target=self.check_res, args=())
                    check_res_thread_list.append(check_res_thread)

                for one in check_res_thread_list:
                    one.start()

                for one in check_res_thread_list:
                    one.join()


if __name__ == "__main__":
    logintest = LoginTest()
    logintest.main()
