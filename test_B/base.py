class BasePacage(object):
    def __init__(self,driver):
        self.driver = driver
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def open_url(self,url):
        self.driver.get(url)
    def quit_url(self):
        self.driver.quit
