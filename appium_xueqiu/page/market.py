#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :market.py
# @Time      :2022/8/4 11:54
# @Author    :Raink
import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.App_base import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):  # 行情
    def goto_search(self):
        # self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()

        return Search(self._driver)


if __name__ == "__main__":
    run_code = 0
