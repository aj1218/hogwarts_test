#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/8/4 10:05
# @Author    :Raink
from time import sleep

from selenium.webdriver.common.by import By

from appium_xueqiu.page.App_base import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        #点击加号
        self.find(By.ID, "post_status").click()
        # 点击行情
        self.find(By.XPATH, "//*[@text='股票']").click()
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/title_text' and @text='市场'] ").click()
        return Market(self._driver)


if __name__ == "__main__":
    run_code = 0
