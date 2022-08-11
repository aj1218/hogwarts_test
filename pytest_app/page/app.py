#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :app.py
# @Time      :2022/7/22 10:26
# @Author    :Raink
from appium import webdriver
from selenium.webdriver.common.by import By

from pytest_app.page.App_base import BasePage
from pytest_app.page.main import Main


class App(BasePage):
    # 启动app
    def start(self):
        if self._driver == None:
            desired_caps = {
                "platformName": "Android",
                "platformVersion": "7.1.2",
                "deviceName": "127.0.0.1:62001",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True,
                "dontStopAppOnReset": True,  # 不退出App
                "automationName": "Uiautomator2",
                "skipDeviceInitialization": True,  # 权限
                "unicodeKeyboard": True,  # 这个和下面那个 这两个关键字是控制中文的输入的
                "resetKeyboard": True
            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            #直接启动app
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    # 重新启动app
    def restart(self):
        pass

    # 退出app
    def stop(self):
        self._driver.quit()

    # 主入口main方法
    def main(self) -> Main:
        return Main(self._driver)
