#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
# from selenium import webdriver
# from time import *
# import json
# import re
# # from selenium_python.config.登录 import DL
# class DL1:
#     dr = webdriver.Chrome()
#     def denglu(self):
#         dr=self.dr
#         dr.get('http://192.168.0.254')
#         dr.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/ul/li[1]/input').clear()
#         dr.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/ul/li[1]/input').send_keys('administrator')
#         dr.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/ul/li[2]/input').send_keys('Bane@7766')
#         asd=dr.find_element_by_id('checkinfo').find_elements_by_tag_name('img')
#         y=''
#         for i in asd:
#             a = i.get_attribute('src')  # 获取标签名中的属性
#             b = re.compile(r'imgs/(.*?).gif')
#             c = b.findall(a)
#             dr.find_element_by_id('input1').send_keys(c)
#
#         dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
#         wasd=dr.switch_to_alert()#切换到弹出框
#         wasd.accept()#点击弹出框上的确定
#
#     # def huoqu(self):
#     #     dr=self.dr
#         a = dr.find_element_by_xpath('//*[@id="Content"]/frame[1]')
#         dr.switch_to_frame(a)
#         dr.find_element_by_xpath('//*[@id="04"]/span[2]').click()
#         dr.find_element_by_xpath('//*[@id="041"]/span').click()
#         dr.switch_to_default_content()
#
#         b = dr.find_element_by_xpath('//*[@id="Content"]/frameset/frame[1]')
#         dr.switch_to_frame(b)
#         dr.find_element_by_xpath('//*[@id="tab_1"]').click()
#         dr.switch_to_default_content()
#
#         c = dr.find_element_by_xpath('//*[@id="main"]')
#         dr.switch_to_frame(c)
#         dr.find_element_by_xpath('//*[@id="body"]/form/table[1]/tbody/tr/td[3]/a').click()
#         sleep(1)
#         dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input').send_keys('zhl')
#         sleep(1)
#         dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div/a').click()
#         sleep(1)
#         w=dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div/p')
#         qwe=w.text
#         print(qwe)
#         # dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div/p').click()
# s=DL1()
# s.denglu()


with open('a.gif','wb')as f:
    f.write('0.7529411764705882 0.7529411764705882 0.7529411764705882')
    f.close()