from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pytest_web.selenium_wxwork_login.register import Register


class Login:
    def __init__(self, driver: WebDriver):  # driver:WebDriver 告诉python这个参数一个webdriver类型的 使用这个参数的时候 可以点出这个类型里面的方法
        # 为了不重写driver 可以直接复用上一个类里面的driver 就是index页面的driver
        self._driver = driver


    def scanf(self):
        # 扫码
        pass

    def goto_register(self):
        # 点击注册按钮  click register
        sleep(5)
        self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register(self._driver)
