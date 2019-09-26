



from appium import webdriver
import unittest
from com.qk.butterly.register.reg import acc_pwd
import re
from time import sleep

class Mytest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('开始测试')

    @classmethod
    def tearDown(self):
        print('已执行所有用例，测试结束')

    def setUp(self):
        print('开始执行此条测试用例')

    def tearDownClass(self):
        print('此条测试用例执行完成')

    def test_a(self):
        reg.acc_pwd()
