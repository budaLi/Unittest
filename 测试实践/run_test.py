from get_data import GetData
from runmain import RunMain
from utils import Utils
from dependData import DependData

class Test:
    def __init__(self):
        self.runMethod = RunMain()
        self.data = GetData()
        self.util = Utils()
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
            print("==============================")
            print("\033[1;45m正在对第%s个测试用例进行测试\033[0m"%i)
            print("-------------------------------")
            is_test = self.data.get_is_test(i)
            #判断是否需要进行测试
            if not is_test:
                continue
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_request_data(i)
            headers = self.data.get_is_headers(i)
            is_depend = self.data.get_depend_id(i)
            if is_depend:
                print("此测试用例有测试依赖")
                self.depend = DependData(is_depend)
                #获取依赖字段
                depend_key = self.depend.get_data_for_key(i)
                #更新数据
                pass

            print("url:{}\nmethod:{}\nheaders:{}\ndata:{},".format(url,method,headers,data))
            print("--------------------------------")
            res = self.runMethod.main(method=method,url=url,data=data,headers=headers)
            self.data.write_actual_value(i,res)

            #测试结果
            expected_data = self.data.get_expected_data(i)
            test_res = self.util.str_is_equal(expected_data,res)
            if test_res:
                self.data.write_test_res(i,"PASS")
            else:
                self.data.write_test_res(i,"NO")

            print("测试结果写入完成")
            print("==============================")
            #指定sortkeys 和indent可使数据更有条理 ensure_ascii可正常显示中文
            # json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__=="__main__":
    test = Test()
    test.run_test()
