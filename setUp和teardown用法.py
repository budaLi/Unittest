# 测试用例类 TestCase 测试用例类就是单个测试单元 其负责检查特定输入和对应的输出是否匹配
# 测试包 TestSuite 用来组合多个测试用例 测试包可以嵌套测试包
# 测试运行器 TestRunner 负责组织 运行测试用例 并向用户呈现测试结果
# 测试固件 Test Fixture 代表执行一个或多个测试用例所需的准备工作 以及相关联的准备操作 准备工作可能包括创建临时数据库 创建目录 开启服务器进程等

# unittest.TestCase 包含了setUp和teardown两个方法 其中setup用于初始化固件 而teardown方法用来销毁测试固件 程序会在每个测试用例(以test_开头的方法)之前
# 自动执行setup 来初始化固件 并在每个测试用例后调用teardown方法销毁固件

import unittest

def add(a,b):
    return a+b

def rem(a,b):
    return a-b

class TestCase(unittest.TestCase):
    def setUp(self):
        print("\n初始化测试固件")
    def tearDown(self):
        print("销毁测试固件")
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertNotEqual(add(1,3),5)
    def test_rem(self):
        self.assertEqual(rem(2,1),1)
        self.assertNotEqual(rem(2,1),0)

#在上面要注意的是 在每个测试类执行之前都执行了setup方法 注意是每个
#如果希望在该类的所有测试用例之前都用一个方法来初始化固件及销毁固件 可以重写setUpclass 函数和teardownclass函数 注意此处要变为类方法


class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("+++++++++++++++++++++++++")
        print("\n初始化测试固件")
    @classmethod
    def tearDownClass(cls):
        print("销毁测试固件")
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertNotEqual(add(1,3),5)
    def test_rem(self):
        self.assertEqual(rem(2,1),1)
        self.assertNotEqual(rem(2,1),0)
if __name__=="__main__":
    unittest.main()

    # python -m unittest -v xxx.py
    # 为该命令添加了 -v 选项，该选项用于告诉 unittest 生成更详细的输出信息