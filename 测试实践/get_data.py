from data_config import *
from operationExcel import OperationExcel
import json

class GetData:
    def __init__(self):
        #初始化操作excel的对象
        self.opExcel =  OperationExcel()

    def get_case_lines(self):
        """
        获取测试用例的个数 第一行为测试标题
        :return:
        """
        lines =  self.opExcel.get_nrows()-1
        return lines

    def get_request_url(self,row):
        """
        获取请求地址
        :param row:
        :return:
        """
        col =getRequestUrlcol()
        request_url = self.opExcel.get_cel_value(row,col)
        return request_url

    def get_request_method(self,row):
        """
        请求方法
        :param row:
        :return:
        """
        col = getRequestMethodcol()
        request_method = self.opExcel.get_cel_value(row,col)
        return request_method

    def get_request_data(self,row):
        """
        请求数据 一般Post请求为json格式 get请求在url中携带
        :param row:
        :return:
        """
        col = getRequestDatacol()
        request_data = self.opExcel.get_cel_value(row,col)
        if request_data=="":
            return None
        #str转json 用json.loads
        data = json.loads(request_data)
        return data

    def get_is_test(self,row):
        """
        判断是否已经测试 或 是否需要测试
        :return:
        """
        col = getIsTestcol()
        is_test = self.opExcel.get_cel_value(row,col)
        if is_test=="Y" or "YES":
            return True
        return False

    def get_is_headers(self,row):
        """
        判断是否使用headers 使用则返回请求头
        :return:
        """
        col = getRequestHeadercol()
        is_headers = self.opExcel.get_cel_value(row,col)
        if is_headers=="":
            return False
        return json.loads(is_headers)


    def get_expected_data(self,row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col =getExpectedResultcol()
        expected_data = self.opExcel.get_cel_value(row,col)
        return expected_data

    # def get_actual_data(self,row):
    #     """
    #     获取实际结果
    #     :param row:
    #     :return:
    #     """
    #     col = getActualResultcol()
    #     actual_data = self.opExcel.get_cel_value(row,col)
    #     return actual_data




