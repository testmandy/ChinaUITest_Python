# coding=utf-8
# @Time    : 2019/5/14 11:10
# @Author  : Mandy

import os
import time
import unittest

from testcases.article import Article

if __name__ == '__main__':
    """
    添加测试套件并运行
    """
    unittest.main(verbosity=2) # 一次执行所有用例
    # test_suite = unittest.TestSuite()  # 创建一个测试集合
    # test_suite.addTest(Article('test_read'))  # 测试套件中添加测试用例
    # test_suite.addTest(Article('test_watch_video'))  # 测试套件中添加测试用例
    # # 打开一个保存结果的html文件
    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "\\ChinaUITest_Python\\report\\" + now + "_result.html"
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ChinaStudy-UI测试报告', description='测试情况')
    # # 生成执行用例的对象
    # runner.run(test_suite)
    # # 执行测试套件
