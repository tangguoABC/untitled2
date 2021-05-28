import time
from selenium import webdriver
from test_B.base import BasePacage

class Baidu_search(object):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    basepeg = BasePacage(driver)

    def open_baidu(self):
        self.basepeg.open_url("https://www.baidu.com")
        time.sleep(1)
    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("Selenium")
        time.sleep(1)
        self.basepeg.back()
        self.basepeg.forward()
        self.basepeg.quit_browser()

b = Baidu_search()
b.open_baidu()
b.test_search()