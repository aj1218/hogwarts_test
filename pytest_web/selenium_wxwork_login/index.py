from selenium.webdriver.common.by import By
from selenium import webdriver

from pytest_web.selenium_wxwork_login.login import Login
from pytest_web.selenium_wxwork_login.register import Register


class Index:

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")

    # 进入登录页面
    def goto_login(self):
        # click login  点击登录的按钮
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)  # return 到login这个PO的页面

    # 进入注册页面
    def goto_register(self):
        # 点击注册按钮  click register
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver) #  避免初始化 driver参数 下传
