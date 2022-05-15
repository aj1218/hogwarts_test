
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, equal_to, close_to, contains_string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestWebdriverWait:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            # "dontStopAppOnReset": True,  # 不退出App
            "automationName": "Uiautomator2",
            "skipDeviceInitialization": True,  # 权限
            "unicodeKeyboard": True,  # 这个和下面那个 这两个关键字是控制中文的输入的
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_search(self):
        '''

        :return:
        1:打开雪球app
        2:点击搜索
        3:输入 搜索词 "alibaba" or "xioami"
        4:点击第一个搜索结果
        5:判断股票价格
        '''





