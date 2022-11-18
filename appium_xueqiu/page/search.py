#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :search.py
# @Time      :2022/8/4 11:57
# @Author    :Raink
from selenium.webdriver.common.by import By

from appium_xueqiu.page.App_base import BasePage


class Search(BasePage):
    def search(self, name):
        self._params["name"] = name
        self.step(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\search.yaml")

    def add(self, name):
        self._params["name"] = name
        self.step(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\search.yaml")

    def is_choose(self,name):  # 验证是否被选中
        self._params["name"] = name
        return self.step(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\search.yaml")

    def reset(self, name):
        self._params["name"] = name
        return self.step(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\search.yaml")
