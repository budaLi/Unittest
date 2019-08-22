# 在默认情况下 unittest会自动测试每一个以test_开头的方法 但是如果希望跳过某个测试用例 可以通过如下两种方式实现
# 1.使用skipXXX装饰器来跳过测试用例 unittest一共提供了三个装饰器 分别是 @unittest.skip(reason),unittest.skipif(condition,reason) ,@unittest.skipUnless(condition,reason)
# 其中skip表示无条件跳过 skipif 表示当条件为true时跳过 skipunless表示条件为False时跳过
# 2、使用TestCase的skipTest()方法来跳过测试用例

import unittest

def add(a,b):
    return a+b

def rem(a,b):
    return a-b

#第一种方法 使用装饰器
class TeatCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertNotEqual(add(1,3),5)
    @unittest.skipIf(1>1,"使用装饰器跳过测试用例")
    def test_rem(self):
        self.assertEqual(rem(2,1),1)
        self.assertNotEqual(rem(2,1),0)

#第二种方法
class TeatCase2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertNotEqual(add(1,3),5)

    def test_rem(self):
        self.skipTest("使用unittest.SkipTest()函数跳过测试用例")
        self.assertEqual(rem(2,1),1)
        self.assertNotEqual(rem(2,1),0)


if __name__=="__main__":
    unittest.main()