import base64
import os


class Utils:
    """
    工具类
    """

    def __init__(self):
        pass

    # def all_path(dirname):
    #
    #     result = []  # 所有的文件
    #
    #     for maindir, subdir, file_name_list in os.walk(dirname):
    #
    #         # print("1:",maindir) #当前主目录
    #         # print("2:",subdir) #当前主目录下的所有目录
    #         # print("3:",file_name_list)  #当前主目录下的所有文件
    #
    #         for filename in file_name_list:
    #             apath = os.path.join(maindir, filename)  # 合并成一个完整路径
    #             ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
    #
    #             if ext in filter:
    #                 result.append(apath)
    #
    #     return result

    def str_is_equal(self, str1, str2):
        """
        判断两个字符串变为字典是否相等
        :param str1:
        :param str2:
        :return: bool
        """
        str1 = str1.replace("true", "True")
        if str1 == "":
            return False
        if not isinstance(str1, dict):
            str1 = eval(str1)
        if not isinstance(str2, dict):
            str2 = eval(str2)
        # print(str1,type(str1))
        # print(str2,type(str2))
        try:
            return str1['returnState']['stateCode'] == str2['returnState']['stateCode']
        except Exception as e:
            print("Error")
            return False

    def is_equal_code(self, code, res):
        """
        检测指定状态码和返回结果状态码是否一致
        :param code:
        :param res:
        :return:
        """
        if not isinstance(res, dict):
            res = eval(res)
        return res['returnState']['stateCode'] == code

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
        if isinstance(password,float):
            password = int(password)
        tem = str(name) + ":" + str(password)
        strs = self.encrypt_by_base64(tem)
        headers = {
            'Authorization': 'Basic ' + strs,  # admin:123456
        }
        return headers


def all_path(dirname):
    result = []  # 所有的文件

    filter = [".xls"]  # 设置过滤后的文件类型 当然可以设置多个类型

    for maindir, subdir, file_name_list in os.walk(dirname):

        # print("1:",maindir) #当前主目录
        # print("2:",subdir) #当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容

            if ext in filter:
                result.append(apath)

    return result


if __name__ == "__main__":
    util = Utils()
    # dic1 ={
    #             "permission": {
    #                 "clusterManage": True,
    #                 "deviceControl": True,
    #                 "deviceManage": True,
    #                 "download": True,
    #                 "opmManage": True,
    #                 "playback": True,
    #                 "systemLog": True,
    #                 "tvmanager": True,
    #                 "userManage": True,
    #                 "view": True
    #             },
    #             "returnState": {
    #                 "errorMsg": 0,
    #                 "stateCode": 0
    #             }
    #         }
    # dic2 ={'permission': {'clusterManage': True, 'deviceControl': True, 'deviceManage': True, 'download': True, 'opmManage': True, 'playback': True, 'systemLog': True, 'tvmanager': True, 'userManage': True, 'view': True}, 'returnState': {'errorMsg': 0, 'stateCode': 0}}
    # import json
    # print(json.dumps(dic1))
    # print(util.str_is_equal(dic1,dic2))
    # print(util.encapsulate_headers('admin','123456'))
    # res=util.get_all_path()
    # print(res)

    res = all_path("C://Users//lenovo//PycharmProjects//自动化测试//测试实践//Excel//test_excel")
    for one in res:
        with open(one) as f:
            print(f.name)


