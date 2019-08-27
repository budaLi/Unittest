#模拟返回数据
from mock import mock
import requests
class Mock:
    """
    封装get和post方法
    """
    def __init__(self):
        self.mock_method= mock.Mock(return_value='{"returnState":{"stateCode":0,"errorMsg":"add error msg"}}')
    def main(self,method,url,data= None,headers = None):
        return self.mock_method(method,url,data, headers)