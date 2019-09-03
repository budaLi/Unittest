# @Time    : 2019/9/2 13:54
# @Author  : Libuda
# @FileName: user_login.py
# @Software: PyCharm

from TestMain.utils import Utils

from TestMain.test_data_config import TestDataConfig


class Login:
    """
    专门为登录测试服务 因为其并不是提交数据 而是将数据封装到请求头中
    """
    def __init__(self,file_name=None):
        self.utils = Utils()
        if file_name:
            self.test_data= TestDataConfig(file_name)
        else:
            self.test_data=TestDataConfig("")
        self.test_res = self.test_data.get_all_test()


    def get_headers(self):
        """
        读取全部测试用例 并将其封装成headers返回
        :return:
        """
        res = []
        if self.test_res:
            for one in self.test_res:
                tem = self.utils.encapsulate_headers(*one)
                res.append(tem)
        return res



if __name__=="__main__":
    log = Login("C:/Users/lenovo/PycharmProjects/自动化测试/测试实践/Excel/test_Login.xls")
    print(log.test_res)
    res = log.get_headers()
    print(res)


