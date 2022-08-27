#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/8/4 10:05
# @Author    :Raink
from time import sleep

import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.App_base import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 点击行情
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='股票']").click()
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/title_text' and @text='市场'] ").click()
        with open(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\main_yaml.yaml", encoding="utf-8") as f:
            steps = yaml.safe_load(f)["goto_market"]
            print(steps)
            for step in steps:
                element = None
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if "click" == action:
                        element.click()
                    if "send" == action:
                        value = step["value"]
                        print(f"send({value})")
        return Market(self._driver)



if __name__ == "__main__":
    run_code = 0
