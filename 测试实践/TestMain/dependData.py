from jsonpath_rw import parse
from TestMain.runmain import RunMain

from TestMain.get_data import GetData


class DependData:
    def __init__(self,depend_id):
        self.depend_id =depend_id
        self.data = GetData()

    def get_depend_data(self):
        """
        无用
        :return:
        """
        row = self.data.get_row_by_depend_id(self.depend_id)
        data = self.data.opExcel.get_data_by_row(row)
        return data

    def run_depend(self):
        """
        运行依赖数据获得其运行结果
        :return:
        """
        self.runmain = RunMain()
        row = self.data.get_row_by_depend_id(self.depend_id)
        url = self.data.get_request_url(row)
        method = self.data.get_request_method(row)
        data = self.data.get_request_data(row)
        headers = self.data.get_is_headers(row)
        res = self.runmain.main(method=method,url=url,data=data,headers=headers)
        return res

    def get_data_for_key(self,row):
        """
        根据依赖的Key去获取执行依赖测试case的相应 然后返回
        :param row:
        :return:
        """
        #依赖数据所属字段
        depend_data = self.data.get_depend_data_belong(row)
        #相应结果数据
        response_data = self.run_depend()
        json_exe = parse(depend_data)
        res = json_exe.find(response_data)
        res = [re.value for re in res][0]
        return res



if __name__=="__main__":
    depend =DependData("3")
    res = depend.run_depend()
    print(res)


