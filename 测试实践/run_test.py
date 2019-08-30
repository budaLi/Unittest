from get_data import GetData
from runmain import RunMain
from mockData import Mock
from utils import Utils
from dependData import DependData
from sendEmail import SendEmail

class Test:
    def __init__(self):
        self.runMethod = RunMain()
        self.data = GetData()
        self.util = Utils()
        self.mock = Mock()
        self.sendemail =SendEmail()

    def run_test(self):
        """
        获取Excel中全部测试用例在对应接口进行测试
        :return:
        """
        #测试用例总数
        row_counts = self.data.get_case_lines()
        #测试个数
        test_num = 0
        #未测试个数
        no_test_num =0

        #测试通过
        test_pass= 0
        #测试未通过
        test_fail=0

        #通过百分比
        pass_percentage = 0.0
        #未通过百分比
        fail_percentage =0.0


        for i in range(1,row_counts+1):
            id = self.data.get_request_id(i)
            is_test = self.data.get_is_test(i)
            #判断是否需要进行测试
            if not is_test:
                no_test_num+=1
                continue
            test_num+=1
            print("==============================================")
            print("\033[1;35m当前测试用例id为:%s\033[0m"%id)
            print("-------------------------------")
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
            # res = self.runMethod.main(method=method,url=url,data=data,headers=headers)
            res = self.mock.main(method=method,url=url,data=data,headers=headers)
            self.data.write_actual_value(i,res)

            #测试结果
            expected_data = self.data.get_expected_data(i)
            test_res = self.util.str_is_equal(expected_data,res)
            if test_res:
                test_pass+=1
                self.data.write_test_res(i,"PASS")
            else:
                test_fail+=1
                self.data.write_test_res(i,"NO")
            import math
            pass_percentage=float(test_pass/(test_pass+test_fail)*100)
            fail_percentage=float(test_fail/(test_pass+test_fail)*100)
            print("测试结果写入完成")
            print("==============================================")

            #指定sortkeys 和indent可使数据更有条理 ensure_ascii可正常显示中文
            # json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        print("\033[1;35m测试完成！\033[0m")
        print("===============================")
        print("\033[1;34m☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆\033[0m")
        print("\033[1;34m☆\033[0m\t\t\t\t\t\033[1;29m测 试 报 告\033[0m\t\t\t\t\t    \033[1;34m☆\033[0m")
        print("\033[1;34m☆\033[0m测试用例总数:\t\t\033[1;36m%s\033[0m\033\t\t\t\t\t\t    \033[1;34m☆\033[0m"%row_counts)
        print("\033[1;34m☆\033[0m未测试个数:\t\t\033[1;35m%s\033[0m \t\t测试个数:\t  \033[1;35m%s\033[0m    \t\033[1;34m☆\033[0m"%(no_test_num,test_num))
        print("\033[1;34m☆\033[0m其中:\t\t\t\t\t\t\t\t\t\t\t    \033[1;34m☆\033[0m")
        print("\033[1;34m☆\033[0m\t通过个数:\t\t\033[1;32m %s \t\033[0m 百分比:\t\t\033[1;32m%.2f%%\033[0m     \033[1;34m☆\033[0m"%(test_pass,pass_percentage))
        print("\033[1;34m☆\033[0m\t失败个数:\t\t\033[1;31m %s \t\033[0m \t 百分比:\t\t\033[1;31m%.2f%%\033[0m     \033[1;34m☆\033[0m"%(test_fail,fail_percentage))
        print("\033[1;34m☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆\033[0m")
        print("\n")
        res = input("是否发送邮件？y/n:\t")
        if res=="y":
            user=[input("请输入收件人邮箱：")]
            if self.sendemail.send_test(user,test_pass,test_fail):
                print("发送成功")


if __name__=="__main__":
    test = Test()
    test.run_test()
