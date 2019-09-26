#!/usr/bin/python
#-*- coding;utf-8 -*_
from selenium import webdriver
from time import sleep
import json
import re
class 登录防火墙():
    dr = webdriver.Chrome()
    def denglu(self):
        dr =self.dr
        dr.get('http://192.168.0.254')
        sleep(1)
        dr.find_element_by_name('txt_password').send_keys('Bane@7766')
        wd=dr.find_element_by_id('checkinfo').find_elements_by_tag_name('img')
        for i in wd:
            a=i.get_attribute('src')#获取标签名中的属性
            b=re.compile(r'imgs/(.*?).gif')
            c=b.findall(a)
            dr.find_element_by_id('input1').send_keys(c)
        sleep(2)
        dr.find_element_by_name('dosubmit').click()
        sleep(2)
        w=dr.switch_to_alert()#切换到弹出框
        w.accept()#点击确定
        sleep(4)
        wd=dr.find_element_by_xpath('/html/frameset/frameset/frame[1]')
        dr.switch_to_frame(wd)
        dr.find_element_by_xpath('//*[@id="04"]').click()
        sleep(1)
        dr.find_element_by_xpath('//*[@id="041"]').click()
        sleep(2)
        dr.switch_to_default_content()
        cd=dr.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]')
        dr.switch_to_frame(cd)
        dr.find_element_by_xpath('//*[@id="nav_1"]').click()
        dr.switch_to_default_content()
        dd = dr.find_element_by_xpath('//*[@id="main"]')
        dr.switch_to_frame(dd)
        sleep(1)
        dr.find_element_by_link_text('按条件查询').click()
        sleep(1)
        dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input').send_keys('zhl')
        dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div/a').click()
        sleep(2)

        # dd = dr.find_element_by_id('main')
        # dr.switch_to_frame(dd)
        m =dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div/p')
        print(m.text)
a =登录防火墙()
a.denglu()
