from get_data import GetData
from runmain import RunMain
import json
class Test:
    def __init__(self):
        self.runMethod = RunMain()
        self.data = GetData()

    def run_test(self):
        """
        获取Excel中全部测试用例在对应接口进行测试
        :return:
        """
        res=None
        row_counts = self.data.get_case_lines()

        #测试写入
        # self.data.opExcel.write_value(3,3,"lsss")

        for i in range(1,row_counts+1):
            is_test = self.data.get_is_test(i)
            #判断是否需要进行测试
            if not is_test:
                continue
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_request_data(i)
            headers = self.data.get_is_headers(i)
            print("url:{},method:{},data:{},".format(url,method,data))
            res = self.runMethod.main(method=method,url=url,data=data,headers=headers)
        #指定sortkeys 和indent可使数据更有条理 ensure_ascii可正常显示中文
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__=="__main__":
    test = Test()
    res=test.run_test()
    print(res)