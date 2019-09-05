from unittest import mock
class Mock:
    """
    模拟响应数据
    """
    def __init__(self):
        self.mock_method= mock.Mock(return_value='{"returnState":{"stateCode":0,"errorMsg":"add error msg"}}')
    def main(self,method,url,data= None,headers = None):
        return self.mock_method(method,url,data, headers)