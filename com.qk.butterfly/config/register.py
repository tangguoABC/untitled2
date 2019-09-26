#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.168.0.0.1:62026 device'
desired_caps['appPackage'] = 'com.qk.butterfly'
desired_caps['appActivity'] = '.main.LauncherActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print('设备初始化成功')
time.sleep(2)


el4 = driver.find_element_by_id("com.qk.butterfly:id/et_login_phone")
el4.send_keys("19937158232")
el5 = driver.find_element_by_id("com.qk.butterfly:id/et_login_code")
el5.send_keys("888888")

driver.save_screenshot('login.png')
driver.get_screenshot_as_file('./images/login.png')

el6 = driver.find_element_by_id("com.qk.butterfly:id/tv_to_login")
el6.click()






