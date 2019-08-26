from data_config import *
from operationExcel import OperationExcel
import json
import xlrd
from xlutils.copy import copy  #写入Excel

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
        # print(request_data)
        #str转json 用json.loads 请求数据用dict
        data = eval(request_data)
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
        #字符串变为字典
        is_headers = eval(is_headers)
        # is_headers={
        #        'Authorization': 'Basic YWRtaW46MTIzNDU2', # admin:123456
        #     }
        return is_headers

    def get_depend_id(self,row):
        """
        根据行号得到依赖ID的内容
        :param row:
        :return:
        """
        col =getDepenIdcol()
        depend_id = self.opExcel.get_cel_value(row,col)
        if depend_id =="":
            depend_id=None
        return depend_id

    def get_depend_data(self,row):
        """
        根据行号得到依赖数据
        :param row:
        :return:
        """
        col = getDependDatacol()
        depend_data = self.opExcel.get_cel_value(row,col)
        return depend_data

    def get_depend_data_belong(self,row):
        """
        根据行号得到依赖数据所属字段
        :param row:
        :return:
        """
        col = getDependDataBelongcol()
        depend_data_belong =self.opExcel.get_cel_value(row,col)
        return depend_data_belong

    def get_row_by_depend_id(self,depend_id):
        """
        根据depend_id的内容找到所依赖的测试ID的行号
        :param depend_id:
        :return:
        """
        row = 1
        test_id_col= getTestIdcol()
        test_id_cols_datas = self.opExcel.get_data_by_col(test_id_col)
        for i in  range(1,len(test_id_cols_datas)):
            if depend_id ==str(int(test_id_cols_datas[i])):
                return row
            row+=1


    def get_expected_data(self,row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col =getExpectedResultcol()
        expected_data = self.opExcel.get_cel_value(row,col)
        return expected_data

    def get_actual_data(self,row):
        """
        获取实际结果
        :param row:
        :return:
        """
        col = getActualResultcol()
        actual_data = self.opExcel.get_cel_value(row,col)
        return actual_data

    def write_actual_value(self,row,value):
        """
        写入实际结果
        :param row:
        :param value:
        :return:
        """
        col = getActualResultcol()
        work_book = xlrd.open_workbook(self.opExcel.file_name)
        #先通过xlutils.copy下copy复制Excel
        write_to_work = copy(work_book)
        # 通过sheet_by_index没有write方法 而get_sheet有write方法
        sheet_data = write_to_work.get_sheet(self.opExcel.sheet_id)
        sheet_data.write(row,col,str(value))
        #这里要注意保存 可是会将原来的Excel覆盖 样式消失
        write_to_work.save(self.opExcel.file_name)

    def write_test_res(self,row,value):
        """
        写入测试结果
        :param row:
        :param value:
        :return:
        """
        col = getTestResultcol()
        work_book = xlrd.open_workbook(self.opExcel.file_name)
        write_to_work = copy(work_book)
        sheet_data = write_to_work.get_sheet(self.opExcel.sheet_id)
        sheet_data.write(row,col,str(value))
        write_to_work.save(self.opExcel.file_name)




