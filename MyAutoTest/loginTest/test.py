import requests
from queue import Queue
import threading
import datetime


class Test:
    def __init__(self):
        self.login_url = "http://10.0.20.245/index/User/login"  # 登录接口
        self.register_url = "http://10.0.20.245/index/User/register"  # 注册接口
        self.test_number = 10  # 测试数量
        self.thread_num = 1  # 开启线程数
        self.start_mobile = 1000000  # 起始手机号 即用户名
        self.register_name = "test"  # 注册用户名 无用
        self.register_pwd = "123456"  # 注册用户密码
        self.register_build = "1"  # 楼栋号
        self.register_unit = "1"  # 单元号
        self.register_room = "1"  # 房间号
        self.basic_register_data = {  # 用户注册模板
            "mobile": "",
            "name": self.register_name,
            "password": self.register_pwd,
            "build": self.register_build,
            "unit": self.register_unit,
            "room": self.register_room
        }
        self.basic_login_data = {  # 登录模板
            "username": "",
            "password": self.register_pwd

        }
        self.register_data_queue = Queue()  # 注册数据
        self.login_queue = Queue()
        self.check_response_queue = Queue()  # 检测队列
        self.gen_register_data()

    def gen_register_data(self):
        """
        生成用户注册及登录数据
        :return:
        """
        for i in range(self.test_number):
            self.start_mobile += 1
            self.register_data_queue.put(str(self.start_mobile))
            self.login_queue.put(str(self.start_mobile))

    def register_user(self):
        """
        用户注册
        :return:
        """
        while not self.register_data_queue.empty():
            mobile = self.register_data_queue.get()
            self.basic_register_data['mobile'] = mobile
            response = requests.post(url=self.register_url, data=self.basic_register_data).json()
            self.check_response_queue.put(response)

    def user_login(self):
        while not self.login_queue.empty():
            mobile = self.login_queue.get()
            self.basic_login_data['username'] = mobile
            response = requests.post(url=self.login_url, data=self.basic_login_data).json()
            self.check_response_queue.put(response)

    def check_res(self):
        success = 0
        fail = 0
        while not self.check_response_queue.empty():
            response = self.check_response_queue.get()
            print(response)
            # if response['code'] == 1:
            #     success += 1
            # else:
            #     fail += 1

        print("success : %s  fail :%s" % (success, fail))

    def main(self):
        key = input("是否注册用户 y/n")
        # 添加用户
        if key == "y":
            add_user_thread_list = []
            for i in range(self.thread_num):
                add_user_thread = threading.Thread(target=self.register_user, args=())
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

                # 状态检测
                check_res_thread_list = []
                for i in range(self.thread_num):
                    check_res_thread = threading.Thread(target=self.check_res, args=())
                    check_res_thread_list.append(check_res_thread)

                for one in check_res_thread_list:
                    one.start()

                for one in check_res_thread_list:
                    one.join()


if __name__ == '__main__':
    test = Test()
    test.main()