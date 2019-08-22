import xlrd
from xlutils.copy import copy  #写入Excel

class OperationExcel():
    """
    #以面向对象的方式操作Excel
    """
    def __init__(self,file_name=None,sheet_id=None):
        """
        初始化OperationExcel对象
        :param file_name:
        :param sheet_id:
        """
        if file_name:
            self.file_name=file_name
            self.sheet_id = sheet_id
        else:
            self.file_name="testDemo.xls"
            self.sheet_id=0
        self.tables=self.get_tables()

    def get_tables(self):
        """
        返回tables对象
        :return:
        """
        ecel = xlrd.open_workbook(self.file_name)
        tables = ecel.sheet_by_index(self.sheet_id)
        return tables

    def get_nrows(self):
        """
        获取表格行数
        :return:
        """
        return self.tables.nrows

    def get_ncols(self):
        """
        获取表格列数
        :return:
        """
        return self.tables.ncols

    def get_cel_value(self,row,col):
        """
        获取某个指定单元格的内容
        :param row:
        :param col:
        :return:
        """
        data =  self.tables.cell_value(row,col)
        return data

    def write_value(self,row,col,value):
        work_book = xlrd.open_workbook(self.file_name)
        #先通过xlutils.copy下copy复制Excel
        write_to_work = copy(work_book)
        # 通过sheet_by_index没有write方法 而get_sheet有write方法
        sheet_data = write_to_work.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        #这里要注意保存 可是会将原来的Excel覆盖 样式消失
        write_to_work.save(self.file_name)

if __name__=="__main__":
    operatinrExcel = OperationExcel()
    print(operatinrExcel.write_value(3,3,2))
