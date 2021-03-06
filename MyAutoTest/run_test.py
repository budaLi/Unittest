import os
from TestMain.get_data import GetData
from TestMain.mockData import Mock
from TestMain.runmain import RunMain
from TestMain.sendEmail import SendEmail
from TestMain.test_data_config import TestDataConfig
from TestMain.utils import Utils
from TestMain.headers import Headers
from templete.specil_Interface import SpecilInterface
from templete.user_login import Login


class Test:
    def __init__(self, test_excel=None, res_excel=None):
        self.runMethod = RunMain()
        # self.data = GetData(test_excel)
        # self.write_data = GetData(r"/home/libuda/PycharmProjects/Unittest/MyAutoTest/Excel/res_excel/testDemo.xls")
        self.write_data = GetData(res_excel)
        self.util = Utils()
        self.test_data = TestDataConfig(test_excel)
        self.mock = Mock()
        self.sendemail = SendEmail()

    def run_test(self):
        """
        获取Excel中全部测试用例在对应接口进行测试
        :return:
        """
        # 测试用例结果
        # all_test = self.test_data.get_all_test()

        # 测试用例总数
        # row_counts = self.data.get_case_lines()
        # row_counts = len(all_test)

        # 测试个数
        test_num = 0
        # 未测试个数
        no_test_num = 0

        # 测试通过
        test_pass = 0
        # 测试未通过
        test_fail = 0

        # 通过百分比
        pass_percentage = 0.0
        # 未通过百分比
        fail_percentage = 0.0

        # 旧版功能

        # for i in range(1,row_counts+1):
        #     id = self.data.get_request_id(i)
        #     is_test = self.data.get_is_test(i)
        #     #判断是否需要进行测试
        #     if not is_test:
        #         no_test_num+=1
        #         continue
        #     test_num+=1
        #     print("==============================================")
        #     print("\033[1;35m当前测试用例id为:%s\033[0m"%id)
        #     print("-------------------------------")
        #     url = self.data.get_request_url(i)
        #     method = self.data.get_request_method(i)
        #     data = self.data.get_request_data(i)
        #     headers = self.data.get_is_headers(i)
        #     is_depend = self.data.get_depend_id(i)
        #     if is_depend:
        #         print("此测试用例有测试依赖")
        #         self.depend = DependData(is_depend)
        #         #获取依赖字段
        #         depend_key = self.depend.get_data_for_key(i)
        #         #更新数据
        #         pass
        #
        #     print("url:{}\nmethod:{}\nheaders:{}\ndata:{},".format(url,method,headers,data))
        #     print("--------------------------------")
        #     # res = self.runMethod.main(method=method,url=url,data=data,headers=headers)
        #     res = self.mock.main(method=method,url=url,data=data,headers=headers)
        #     self.data.write_actual_value(i,res)
        #
        #     #测试结果
        #     expected_data = self.data.get_expected_data(i)
        #     test_res = self.util.str_is_equal(expected_data,res)
        #     if test_res:
        #         test_pass+=1
        #         self.data.write_test_res(i,"PASS")
        #     else:
        #         test_fail+=1
        #         self.data.write_test_res(i,"NO")
        #     pass_percentage=float(test_pass/(test_pass+test_fail)*100)
        #     fail_percentage=float(test_fail/(test_pass+test_fail)*100)
        #     print("测试结果写入完成")
        #     print("==============================================")

        # 新版功能
        name = self.test_data.get_test_name()  # 测试功能
        url = self.test_data.get_test_url()  # 测试接口
        method = self.test_data.get_test_method()  # 测试方法

        all_test = self.test_data.get_all_test()  # 所有测试用例

        if url.split("=")[-1] == "UserLogin":
            login_headers = Login(file_name=r"D:\PycharmProjects\AutoTest\MyAutoTest\Excel\test_excel\test_Login.xls")
            headers = login_headers.get_headers()  # 请求头在登录时生成

        else:
            # 为满足登录要求的headers形式将统一的headers加长
            try:
                with open("header.json", 'r') as f:
                    header = eval(f.read())
                    # print("读取headers",header)
            except Exception as e:
                print("读取异常")

            # 在这里要根据每个测试用力提交的数据长度 更新content-length
            headers = []
            for one_test in all_test:
                header['Content-Length'] = len(one_test)
                headers.append(header)

        self.specil_Interface = SpecilInterface(url)
        tem_data = self.specil_Interface.all_func(*all_test)

        if tem_data:  # 是特殊请求数据格式
            all_test = tem_data
        else:  # 否则按照正常字典构建
            all_test = self.test_data.refactor_all_test()

        row_counts = len(all_test)  # 测试用例个数

        note = self.test_data.get_note()  # 测试备注
        statecode = self.test_data.get_statecode()  # 状态码

        # 在这里要解决的问题是 指定多个测试文件时该如何写入
        lines = self.write_data.get_write_lines()  # 获取Excel中第一个空行的行号
        for i in range(row_counts):
            # 模拟相应
            response = self.mock.main(method, url, all_test[i], headers[i])
            # 真实响应
            # response = self.runMethod.main(method, url, all_test[i], headers[i])
            state = int(statecode[i])
            test_res = "Fail"
            if self.util.is_equal_code(state, response):
                test_pass += 1
                test_res = "Pass"

                # 获取正确登录的用户名和密码的请求头 auth-token
                # 登录成功 headers可用
                if state == 0 and url.split("=")[-1] == "UserLogin":
                    hed = Headers(url, headers[i])
                    # hed.get_headers()
                    # print("生成headr",self.headers)
            else:
                test_fail += 1
            self.write_data.write_all_data(lines, lines, name, url, method, str(headers[i]), str(all_test[i]), note[i],
                                           state, str(response), test_res)
            lines += 1

        pass_percentage = float(test_pass / (test_pass + test_fail) * 100)
        fail_percentage = float(test_fail / (test_pass + test_fail) * 100)

        # print("测试完成!")
        # print("===============================")
        # print("\033[1;34m☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆\033[0m")
        # print("\033[1;34m☆\033[0m\t\t\t\t\t\033[1;29m测 试 报 告\033[0m\t\t\t\t\t    ")
        # print("\033[1;34m☆\033[0m测试用例总数:\t\t\033[1;36m%s\033[0m\033\t\t\t\t\t\t    "%row_counts)
        # print("\033[1;34m☆\033[0m未测试个数:\t\t\033[1;35m%s\033[0m \t\t测试个数:\t  \033[1;35m%s\033[0m   "%(no_test_num,test_num))
        # print("\033[1;34m☆\033[0m其中:\t\t\t\t\t\t\t\t\t\t\t   ")
        # print("\033[1;34m☆\033[0m\t通过个数:\t\t\033[1;32m %s \t\t\033[0m 百分比:\t\t\033[1;32m%.2f%%\033[0m    "%(test_pass,pass_percentage))
        # print("\033[1;34m☆\033[0m\t失败个数:\t\t\033[1;31m %s \t\033[0m \t 百分比:\t\t\033[1;31m%.2f%%\033[0m   "%(test_fail,fail_percentage))
        # print("\033[1;34m☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆\033[0m")
        # print("\n")
        # res = input("是否发送邮件？y/n:\t")
        # if res=="y":
        #     user=[input("请输入收件人邮箱：")]
        #     if self.sendemail.send_test(user,test_pass,test_fail):
        #         print("发送成功")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="脚本信息描述")
    parser.add_argument("-f", "--filepath", help="测试用例文件夹",default="./Excel/test_excel/")
    parser.add_argument("-r", "--respath", help="测试结果",default="./Excel/res_excel/testDemo.xls")
    args = vars(parser.parse_args())  # vars() 函数返回对象object的属性和属性值的字典对象。
    # print(args['filepath'])  #获取输入的测试用例文件路径

    root_dir = "./Excel/test_excel/"
    # 定义测试的顺序

    # 用户管理
    user_manage = ["test_Login.xls","test_UserAddUser.xls","test_QueryUserList.xls","test_ChangePassword.xls","test_DeleteUser.xls"]
    # 集群管理
    node_manage = ["test_SearchNodeList.xls","test_AddNotes.xls","test_DeleteNotes.xls","test_ModifyNodeInfo.xls","test_QueryNodeList.xls",
                   "test_SetNtpServer.xls","test_QueryNtpServer.xls","test_SetVmsInfo.xls","test_QueryVmsInfo.xls"]

    # 任务管理
    task_manage = ["test_QueryTaskList.xls"]
    # 运维管理
    operations_manage = ["test_QueryAllResiyrceInfo.xls"]
    # 日志管理
    log_manage = ["test_GetServerLog.xls"]

    # 总的测试任务
    all_task = []
    all_task.extend(user_manage)
    all_task.extend(node_manage)
    all_task.extend(task_manage)
    all_task.extend(operations_manage)
    all_task.extend(log_manage)

    res_excels = args['respath']
    for test_excel in all_task:
            path = os.path.join(root_dir,test_excel)
            print("正在对 %s 进行测试" % test_excel.split("/")[-1])
            test = Test(path, res_excels)
            test.run_test()


    # test = Test(r"C:\Users\lenovo\PycharmProjects\AutoTest\MyAutoTest\Excel\test_excel\test_UserAddUser.xls")
    # # test = Test()
    # test.run_test()
