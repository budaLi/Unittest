import requests
import base64
import threading
import datetime
from queue import Queue


class Utils:
    
    def encrypt_by_base64(self, strs):
        """
        ���ַ�������base64����
        :param strs:
        :return:
        """
        # ���������Ĵ��������byte���ʶ�ԭ����Ҫ�ȱ��룬ʹԭ����str���ͱ��byte�������ֱ�����������byte���󣬹�Ҫ�����str����
        strs = base64.b64encode(strs.encode())
        res = strs.decode()
        return res

    def encapsulate_headers(self, name, password):
        """
        �����뼰headers���з�װ
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
        self.init_proxy_ip = "http://20.0.88.%s:80"  # ��ʼip
        self.max_use = 50  # ÿ��ip���ʹ�ô���
        self.proxy_pools = self.gen_proxy_pool(num=20)  # ����ip  num  ����ip����
        self.add_user_queue = Queue()  # ����û���Ϣ����
        self.login_header_queue = Queue()  # ��¼����ͷ����
        self.check_response_queue = Queue()  # ���response����
        self.del_user_queue = Queue()  # ɾ���û�����
        self.init_user_id = 100000  # �û���ʼid
        self.init_user_pwd = "123456"  # �û�����Ĭ������
        self.functionalRoleList = ""  # �û�Ĭ�Ͻ�ɫ�б�
        self.resourceRoleList = ""  # �û�Ĭ����Դ�б�
        self.content_length = "123"  # Ĭ������û������ֶγ���
        self.add_user_num = 100  # Ĭ������û���
        self.login_user_num = self.add_user_num  # Ĭ�ϵ�¼�û���
        self.thread_num = int(self.add_user_num / 10) if self.add_user_num < 100 else int(
            self.add_user_num / 100)  # Ĭ�Ͽ����߳���
        self.user_name_prefix = "li"
        self.utils = Utils()
        self.login_name = "admin"  # ��¼�û���
        self.login_pwd = "123456"  # ��¼����
        self.login_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin"  # ��¼�ӿ�
        self.add_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser"  # ����û��ӿ�
        self.del_user_url = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserDeleteUser"  # ɾ���û��ӿ�
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
        self.del_user_header = self.add_user_header  # ɾ���û�����ͷ

    def get_add_user_headers(self):
        """
        ģ���¼��ȡauthtoken
        :return:
        """
        response_headers = requests.post(url=self.login_url, headers=self.login_headers).headers

        self.init_add_user_header['Auth-Token'] = response_headers["auth-token"]  # ��¼��ȡauthtoken
        return self.init_add_user_header

    def gen_proxy_pool(self, num):
        """
        ip�����
        :param num:  ����ip����
        :return:
        """
        proxy_pools_queue = Queue()
        for i in range(num):
            for _ in range(self.max_use):
                proxy_pools_queue.put(self.init_proxy_ip % str(i))
        return proxy_pools_queue

    def check_res(self):
        """
        ״̬���
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
        �����û���Ϣ
        :param user_id: ��ʼ�û�id
        :param max_num: �����û�����
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
        ����û�
        :return:
        """
        while not self.add_user_queue.empty():
            user_data = self.add_user_queue.get(timeout=3)
            response = requests.post(url=self.add_user_url, data=user_data, headers=self.add_user_header)
            self.check_response_queue.put(response.json())

    def user_login(self):
        """
        �û���¼
        :return:
        """
        proxies = ""

        while not self.login_header_queue.empty():
            headers = self.login_header_queue.get()
            if not self.proxy_pools.empty():
                proxies = self.proxy_pools.get()
            proxy_dict = {
                'http': proxies,  # ע��˴���http��ip
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
        ɾ���û�
        :return:
        """
        while not self.del_user_queue.empty():
            user_id = self.del_user_queue.get()
            response = requests.post(url=self.del_user_url, data='{"userID": "%s"}' % str(user_id),
                                     headers=self.add_user_header)
            self.check_response_queue.put(response.json())

    def main(self):
        key = input("�Ƿ�����û� y/n")
        # ����û�
        if key == "y":
            print("����û���")
            self.generate_user_info(self.init_user_id, self.add_user_num)
            add_user_thread_list = []
            for i in range(self.thread_num):
                add_user_thread = threading.Thread(target=self.add_user, args=())
                add_user_thread_list.append(add_user_thread)

            for one in add_user_thread_list:
                one.start()
            for one in add_user_thread_list:
                one.join()

            print("������")

            key = input("�Ƿ���е�¼���� y/n")
            if key == "y":
                # ��¼����
                print("��ʼ��¼����")
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

                print("��¼�������")

            key = input("�Ƿ����ɾ������ y/n")
            if key == "y":
                # ɾ���û�
                print("��ʼɾ������")
                user_del_thread_list = []
                for i in range(self.thread_num):
                    user_del_thread = threading.Thread(target=self.del_user, args=())
                    user_del_thread_list.append(user_del_thread)

                for one in user_del_thread_list:
                    one.start()
                for one in user_del_thread_list:
                    one.join()
                print("ɾ���������")

                # ״̬���
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
