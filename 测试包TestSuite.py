#测试包可以组织多个测试用例 测试包还可以嵌套测试包
# 在使用测试包组织多个测试用例和测试包后 程序可以使用测试运行器 TestRunner 来运行该测试包包含的所有测试用例
import unittest
import HTMLTestRunner

def say_hello():
    return "hello world"

def add(a,b):
    return a+b


class Test1(unittest.TestCase):
    #测试say_hellO()函数
    def test_say_hello(self):
        self.assertEqual(say_hello(),"hello world")
    #测试加法
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(3,4),7)
        self.assertEqual(add(-1,2),1)


#第二个测试包

def say_byby():
    return "byby"

def mult(a,b):
    return a*b


class Test2(unittest.TestCase):
    def test_say_byby(self):
        self.assertEqual(say_byby(),"byby")
    def test_mult(self):
        self.assertEqual(mult(1,3),3)
        self.assertEqual(mult(2,3),6)
        self.assertEqual(mult(3,3),9)


test_cases=(Test1,Test2)

def whole_suite():
    #创建测试加载器
    loader = unittest.TestLoader()
    #创建测试包
    suite =unittest.TestSuite()

    for test_class in test_cases:
        #从测试类中加载测试用例
        tests= loader.loadTestsFromTestCase(test_class)
        #将测试用例添加到测试包
        suite.addTest(tests)
    return suite


if __name__=="__main__":
    #创建测试运行器
    # with open("out.txt",'w') as f:
    #     runner =unittest.TextTestRunner(verbosity=2,stream=f)
    #     suite=whole_suite()
    #     runner.run(suite)
    with open("./out.html",'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f,title="这是一个报告")
        suite = whole_suite()
        print(suite)
        runner.run(suite)