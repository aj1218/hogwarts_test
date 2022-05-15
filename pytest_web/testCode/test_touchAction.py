from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver import TouchActions

class TestActionChains():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        """
        实现以下内容：
        打开URL：http://www.baidu.com
        向搜索框中输入“selenium测试”
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        """
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element(By.ID, "kw")
        print("11111111113",type(el))
        el_search = self.driver.find_element(By.ID, "su")
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll_from_element(el, 0, 10000).perform()
        sleep(3)

