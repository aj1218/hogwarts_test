import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cook")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:  # 遍历循环字典中的cookies 然后加入到请求的cookies中
            if "expiry" in cookie.keys():  # 如果发现这个expiry在cookes中 就把他拿走 去实现cookies的免登录
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        print(self.driver.get_cookies())  # 获取浏览器中所有的cookies
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(4)
        db.close()



