# @Time    : 2019/9/2 12:01
# @Author  : Libuda
# @FileName: specil_Interface.py
# @Software: PyCharm
import json


class SpecilInterface:
    """
    为特殊的接口提供数据请求模板
    """

    def __init__(self, name):
        # 请求数据较为特殊的接口
        self.name = name
        self.special_name = {'UserAddUser', 'UserAddRole'}

    def all_func(self, *args):
        """
        如果为特殊接口 返回构造请求 不是则返回None
        :param args:
        :return:
        """
        if self.name == "UserAddUser":
            res = []
            for user in args:
                tem = '{"accountInfo":{"userID":"%s","username":"%s","password":"%s",' \
                      '"functionalRoleList":"%s","resourceRoleList":"%s"}}' % user
                res.append(tem + ":")

                # 提交的data 长度存在问题

                # user = tuple(user)
                # dic = {}
                # dic["accountInfo"]={}
                # dic['accountInfo']['userID'] = user[0]
                # dic['accountInfo']['username'] = user[1]
                # dic['accountInfo']['password'] = user[2]
                # dic['accountInfo']['functionalRoleList'] = user[3]
                # dic['accountInfo']['resourceRoleList'] = user[4]
                # tem= json.dumps(dic)
                # res.append(tem)

            return res
        else:
            return None


if __name__ == "__main__":
    s = SpecilInterface('UserAddUser')
    kes = ('xx', 'xx', 'xx', 'xx', 'x')
    res = s.all_func(kes)[0]
    print(type(res))
