#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/7/25 16:11
# @Author    :Raink
from time import sleep

from selenium.webdriver.common.by import By

from pytest_app.page_UI.base_page import BasePage


class Main(BasePage):

    def goto_search(self):
        sleep(2)
        # self.find(By.ID, "com.xueqiu.android:id/home_search").click()
        self.steps(r"D:\pythonProject\hogwarts_test\pytest_app\page_UI\main.yaml")

    def goto_windows(self):
        self.find(By.ID,"post_status").click()
        self.find(By.ID, "com.xueqiu.android:id/home_search").click()


if __name__ == "__main__":
    run_code = 0
