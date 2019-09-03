# @Time    : 2019/9/2 10:53
# @Author  : Libuda
# @FileName: test_data_config.py
# @Software: PyCharm
from TestMain.operationExcel import OperationExcel
from templete.specil_Interface import SpecilInterface
class TestDataConfig:
    """
    测试用例中各列对应行号及列号   还需要为特殊的请求数据构造对应的请求内容
    """

    def __init__(self,file_name=None):
        if file_name is None:
            file_name= ""
        self.opExcel = OperationExcel(file_name,0)

        self.test_name = [0, 1]  # 测试功能行列
        self.test_url = [1, 1]  # 测试接口行列
        self.test_method = [2, 1]  # 测试方法行列
        self.test = 4      #测试用例所在行
        self.test_ziduan_num = [3, 1]  # 测试字段个数 每个测试功能字段数量不固定
        self.test_zidaun_init_position = [5, 2]  # 测试字段起始行号及列号
        self.test_num = self.get_test_num()    #测试用例的个数

        # 备注 需要根据测试字段个数求出
        self.test_note = self.get_note_col()

        #测试状态码列号为测试备注的列号加一
        self.test_statecode = self.test_note+1

    def get_test_name(self):
        """
        测试功能
        :return:
        """
        return self.opExcel.get_cel_value(*self.test_name)

    def get_test_url(self):
        """
        测试接口
        :return:
        """
        return self.opExcel.get_cel_value(*self.test_url)

    def get_test_method(self):
        """
        测试方法
        :return:
        """
        return self.opExcel.get_cel_value(*self.test_method)

    def get_test_note(self,row):
        """
        测试备注
        :return:
        """
        return self.opExcel.get_cel_value(row,self.get_note_col())

    def get_test_statecode(self,row):
        """
        预期结果状态码
        :return:
        """
        return self.opExcel.get_cel_value(row,self.test_statecode)

    def get_test_ziduan_num(self):
        """
        测试字段个数的值
        :return:
        """
        return int(self.opExcel.get_cel_value(*self.test_ziduan_num))

    def get_zidaun_name(self):
        """
        测试字段的属性值 以列表形式返回
        :return:
        """
        res=[]
        row = self.test
        for i in range(self.test_zidaun_init_position[1],self.test_zidaun_init_position[1]+self.get_test_ziduan_num()):
            res.append(self.opExcel.get_cel_value(row,i))
        return res


    def get_test_num(self):
        """
        获取测试用例的个数
        :return:
        """
        #先求表格的行数  已知前面几行
        col_num = self.opExcel.get_nrows()
        test_num = col_num - 5
        return test_num

    def get_note_col(self):
        """
        获取备注的列号
        :return:
        """
        #先求出字段个数
        # num =self.opExcel.get_cel_value(self.test_ziduan_num[0],self.test_ziduan_num[1])
        num =self.opExcel.get_cel_value(*self.test_ziduan_num)
        if isinstance(num,int):
            num=int(num)
        note_col = 2 + num
        return int(note_col)

    def get_all_test(self):
        """
        获取所有测试用例 以列表形式返回
        :return:
        """
        tem=[]
        row = self.test + 1
        for i in range(self.test_num):
            s=[]
            for j in range(self.test_zidaun_init_position[1], self.test_zidaun_init_position[1] + self.get_test_ziduan_num() ):
                s.append(self.opExcel.get_cel_value(row, j))
            tem.append(s)
            row += 1
        return tem


    def get_note(self):
        """
        获取备注
        :return:
        """
        res=[]
        row = self.test + 1
        for i in range(self.test_num):
            tem=self.opExcel.get_cel_value(row,self.test_note)
            res.append(tem)
            row += 1
        return res

    def get_statecode(self):
        """
        获取状态码
        :return:
        """
        res=[]
        row = self.test + 1
        for i in range(self.test_num):
            tem=self.opExcel.get_cel_value(row,self.test_statecode)
            res.append(tem)
            row += 1
        return res


    def refactor_all_test(self):
        """
        将测试用例用对应字段属性进行构建
        :return:
        """

        tem=self.get_all_test()
        row = self.test
        ziduan_name = self.get_zidaun_name()
        test_url = self.opExcel.get_cel_value(*self.test_url)
        specilname = SpecilInterface(test_url)
        res = specilname.all_func(*tem)
        if res:
            return res
        else:
            res=[]
            for i in range(len(tem)):
                dic = dict(zip(ziduan_name,tem[i]))
                res.append(dic)
            return res


if __name__=="__main__":
    testDataConfig = TestDataConfig(r"C:\Users\lenovo\PycharmProjects\AutoTest\MyAutoTest\Excel\test_excel\test_Login.xls")
    res = testDataConfig.get_zidaun_name()
    # print(res)
    res2 = testDataConfig.get_all_test()
    print(res2)

    res3 = testDataConfig.refactor_all_test()
    for one in res3:
        print(one)

    res4 = testDataConfig.get_note()
    print(res4)