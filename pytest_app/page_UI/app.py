#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :app.py
# @Time      :2022/7/25 15:59
# @Author    :Raink
from appium import webdriver

from pytest_app.page_UI.base_page import BasePage
from pytest_app.page_UI.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        # 不想每一次都重新初始化这个slef._driver在第二次调用start的时候，进行一个复用
        if self._driver is None:
            desired_caps = {
                "platformName": "Android",
                "platformVersion": "7.1.2",
                "deviceName": "127.0.0.1:62001",
                "appPackage": self._package,
                "appActivity": self._activity,
                "noReset": True,  # 不清空数据
                "dontStopAppOnReset": True,  # 不退出App
                "automationName": "Uiautomator2",
                "skipDeviceInitialization": True,  # 权限
                "unicodeKeyboard": True,  # 这个和下面那个 这两个关键字是控制中文的输入的
                "resetKeyboard": True
            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(10)

        else:
            self._driver.start_activity(self._package, self._activity)  # 如果有self._driver，直接启动对应的包和activity

        return self

    def Main(self) -> Main:
        return Main(self._driver)


if __name__ == "__main__":
    run_code = 0
