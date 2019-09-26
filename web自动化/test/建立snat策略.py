#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
from selenium import webdriver
import unittest
from web自动化.data.duqu import duqu
import re
from web自动化.config import web登录
from time import sleep
a=web登录.登录防火墙()
b=duqu()
c=b.du()
class 新建策略1(unittest.TestCase):
    def setUp(self):
        a.denglu()
    def test_1(self):
        a.xinjian(c[0])
        self.assertEqual(a.chaxun(c[0]),c[0][8])
    def test_2(self):
        self.assertEqual(a.xinjian(c[1]),c[1][8])
    def test_3(self):
        self.assertEqual(a.xinjian(c[2]),c[2][8]+'\n')
    def test_4(self):
        self.assertEqual(a.xinjian(c[3]),c[3][8])
    def test_5(self):
        self.assertEqual(a.xinjian(c[4]),c[4][8])
    def test_6(self):
        self.assertIn(c[0][3],a.houtai())

