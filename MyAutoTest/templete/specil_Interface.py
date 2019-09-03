# @Time    : 2019/9/2 12:01
# @Author  : Libuda
# @FileName: specil_Interface.py
# @Software: PyCharm
class SpecilInterface:
    """
    为特殊的接口提供数据请求模板
    """
    def __init__(self,name):
        #请求数据较为特殊的接口
        self.name = name
        self.special_name = {'UserAddUser','UserAddRole'}
    def all_func(self,*args):
        """
        如果为特殊接口 返回构造请求 不是则返回None
        :param args:
        :return:
        """
        if self.name=="UserAddUser":
            res= []
            for one in args:
                one = tuple(one)
                tem = '{"accountInfo":' \
                            '{"userID":%s,"username":%s,"password":%s,' \
                             '"functionalRoleList":[,{ "functionalRole":%s }], ' \
                                 '"resourceRoleList":[{ "resourceRole":%s ] }}'%(one)

                # tem = {"accountInfo":
                #             {"userID":1,"username":1,"password":1,
                #              "functionalRoleList":[{ "functionalRole":1 }],
                #                  "resourceRoleList":[ { "resourceRole":1 }],
                #              }
                #        }

                res.append(tem)

            return res
        else:
            return None


if __name__=="__main__":
    s = SpecilInterface('UserAddUser')
    kes = ('xx', 'xx', 'xx', 'xx', 'x')
    res = s.all_func(kes)
    print(res)

