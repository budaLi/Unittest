from TestMain.runmain import RunMain
import requests
import json


class Headers:
    """
    维护一个可正常访问接口的headers
    """

    def __init__(self, url, headers):
        self.count = 0  # 统计get_headers次数 避免服务器异常陷入死循环
        self.url = url
        self.data = ""
        self.headers = headers
        self.runmain = RunMain()

    def get_headers(self):
        """
        模拟登录重新获取headers
        :return:
        """
        headers = requests.post(url=self.url, data="", headers=self.headers).headers
        if self.check_headers(headers):
            headers2 = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Auth-Token': "",
                'Accept-Language': 'zh-CN',
                'Connection': 'keep-alive',
                'Content-Length': "121",
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': '10.0.20.126',
                'Referer': 'http://10.0.20.126/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
            }
            with open("header.json", 'w') as f:
                headers2['Auth-Token'] = headers["auth-token"]
                # tem={'Auth-Token':str(headers["auth-token"])}
                json.dump(headers2, f)
                # f.write("{'Auth-Token':"+"'"+str(headers.headers["auth-token"])+"'"+"}")
        else:
            if self.count >= 5:
                return None
            self.count += 1
            return self.get_headers()

    def check_headers(self, headers):
        """
        模拟访问其他接口判断该headers是否可用
        :param headers:
        :return:
        """
        return True
        # url = "http://10.0.20.126/VMS2Service.cgi?Cmd=AlarmQuerySystemAlarm"
        # response = requests.post(url, data="", headers=self.headers)
        # print(response.text)
        # if response == 200:
        #     return True
        # return False


if __name__ == "__main__":
    head = Headers("http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin", {'Authorization': 'Basic YWRtaW46MTIzNDU2'})
    head.get_headers()
    headers2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Auth-Token': '1568137083',
        'Accept-Language': 'zh-CN,',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '10.0.20.126',
        'Referer': 'http://10.0.20.126/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    try:
        with open("header.json", 'r') as f:
            header = f.read()
            print("读取headers", header)
    except Exception as e:
        print("读取异常")
    response = requests.post(url="http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser",
                             data='{"accountInfo":{"userID":100000,"username":libuda,"password":123456,"functionalRoleList":[,{ "functionalRole": }], "resourceRoleList":[{ "resourceRole": ] }}:',
                             headers=eval(header))

    print(response.text)

    s = '{"accountInfo":{"userID":100000,"username":"libuda","password":"233333","functionalRoleList":[{ "functionalRole":"" }], "resourceRoleList":[{ "resourceRole":"" ] }}'
    s2 = '{"accountInfo":{"userID":"100000","username":"libuda","password":"123456","functionalRoleList":"","resourceRoleList":""}}'
    ss =json.dumps(s2)
    print(type(s))
    print("ss",len(ss))
    s3 = '{"accountInfo":{"userID":"100000","username":"libuda","password":"123456","functionalRoleList":"","resourceRoleList":""}}:'
    print(len(s2))
    print(len(s3))
