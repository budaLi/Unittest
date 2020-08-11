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
        self.special_name = {'UserAddUser', 'ADDNODES',"MODIFYNODEINFO","SETNTPSERVER","SETVMSINFO"}

    def all_func(self, *args):
        """
        如果为特殊接口 返回构造请求 不是则返回None
        :param args:
        :return:
        """
        res = []
        if self.name == "UserAddUser":
            for user in args:
                # tem = '{"accountInfo":{"userID":"%s","username":"%s","password":"%s",' \
                #       '"functionalRoleList":"%s","resourceRoleList":"%s"}}' % user
                # res.append(tem + ":")

                # 提交的data 长度存在问题

                user = tuple(user)
                dic = {}
                dic["accountInfo"]={}
                dic['accountInfo']['username'] = user[0]
                dic['accountInfo']['password'] = user[1]
                dic['accountInfo']['permission'] = user[2]
                tem= json.dumps(dic)
                res.append(tem)
        elif self.name == "ADDNODES":
            for node in args:
                node = tuple(node)
                dic = {}
                dic["nodeList"]={}
                dic['nodeList']['guid'] = node[0]
                dic['nodeList']['ip'] = node[1]
                dic['nodeList']['name'] = node[2]
                tem= json.dumps(dic)
                res.append(tem)

            return res

        elif self.name =="MODIFYNODEINFO":
            for node in args:
                node = tuple(node)
                dic = {}
                dic["nodeInfo"]={}
                dic['nodeInfo']['guid'] = node[0]
                dic['nodeInfo']['name'] = node[1]
                tem= json.dumps(dic)
                res.append(tem)

        elif self.name == "SETNTPSERVER":
            for node in args:
                node = tuple(node)
                dic = {}
                dic["ntpConfig"] = {}
                dic['ntpConfig']['ntpServerIP'] = node[0]
                dic['ntpConfig']['syncInterval'] = node[1]
                dic['ntpConfig']['enableSync'] = node[2]
                tem = json.dumps(dic)
                res.append(tem)

        elif self.name == "SETVMSINFO":
            for node in args:
                node = tuple(node)
                dic = {}
                dic["ntpConfig"] = {}
                dic['ntpConfig']['ip'] = node[0]
                dic['ntpConfig']['port'] = node[1]
                dic['ntpConfig']['username'] = node[2]
                dic['ntpConfig']['password'] = node[3]
                tem = json.dumps(dic)
                res.append(tem)

            return res
        else:
            return None


if __name__ == "__main__":
    s = SpecilInterface('ADDNODES')
    kes = ('xx', 'xx', 'xx', 'xx', 'x')
    res = s.all_func(kes)[0]
    print(res)
