import unittest
#pyunit具有如下特征
#使用断言方法判断期望值和实际值的差异 返回bool值

#所有测试的本质都是一样的 都是通过给定参数来执行函数 然后判断函数的实际输出结果与期望输出结果是否一致

#测试驱动开发  这种方式强调先编写测试用例 然后再编写函数和方法
# 假如程序要开发满足 A 功能的 fun_a() 函数，采用测试驱动开发的步骤如下：
# 1. 为 fun_a() 函数编写测试用例，根据业务要求，使用大量不同的参数组合来执行 fun_a() 函数，并断言该函数的执行结果与业务期望的执行结果匹配。
# 2.编写、修改 fun_a() 函数。
# 3.运行 fun_a() 函数的测试用例，如果测试用例不能完全通过；则重复第 2 步和第 3 步，直到 fun_a() 的所有测试用例全部通过。

#测试驱动开发强调结果导向 也就是在开发某个功能之前 先定义好该功能的最终结果 然后再去开发该功能

#unittest要求单元测试类必须继承 unittest.Test 该类中的测试方法有如下要求
#1.测试方法应该没有返回值
#2.测试方法不应该有任何参数
#3.测试方法发应该以test开头

# 常用断言方法	检查条件
# assertEqual(a, b)	a == b
# assertNotEqual(a, b)	a != b
# assertTrue(x)	bool(x) is True
# assertFalse(x)	bool(x) is False
# assertIs(a, b)	a is b
# assertIsNot(a, b)	a is not b
# assertIsNone(x)	x is None
# assertIsNotNone(x)	x is not None
# assertIn(a, b)	a in b
# assertNotIn(a, b)	a not in b
# assertlsInstance(a, b)	isinstance(a, b)
# assertNotIsInstance(a, b)	not isinstance(a, b)


# 除了上面这些断言方法，如果程序要对异常、错误、警告和日志进行断言判断，TestCase 提供了如表 2 所示的断言方法。
# 断言方法	检查条件
# assertRaises(exc, fun, *args, **kwds)	fun(*args, **kwds) 引发 exc 异常
# assertRaisesRegex(exc, r, fun, *args, **kwds)	fun(*args, **kwds) 引发 exc 异常，且异常信息匹配 r 正则表达式
# assertWarns(warn, fun, *args, **kwds)	fun(*args, **kwds) 引发 warn 警告
# assertWamsRegex(warn, r, fun, *args, **kwds)	fun(*args, **kwds) 引发 warn 警告，且警告信息匹配 r 正则表达式
# assertLogs(logger, level)	With 语句块使用日志器生成 level 级别的日志

# TestCase 断言方法用于完成某种特定检查。
# 断言方法	检查条件
# assertAlmostEqual(a, b)	round(a-b, 7) == 0
# assertNotAlmostEqual(a, b)	round(a-b, 7) != 0
# assertGreater(a, b)	a > b
# assertGreaterEqual(a, b)	a >= b
# assertLess(a, b)	a < b
# assertLessEqual(a, b)	a <= b
# assertRegex(s, r)	r.search(s)
# assertNotRegex(s, r)	not r.search(s)
# assertCountEqual(a, b)	a、b 两个序列包含的元素相同，不管元素出现的顺序如何

# ．：代表测试通过。
# F：代表测试失败，F 代表 failure。
# E：代表测试出错，E 代表 error。
# s：代表跳过该测试，s 代表 skip。


def add(a,b):
    return a+b

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始')
    def test_01(self):
        self.assertNotEqual(add(1,2),4)
    def test_02(self):
        self.assertEqual(add(1,2),3)

    @classmethod
    def tearDownClass(cls):
        print('结束')


if __name__=="__mian__":
    unittest.main()