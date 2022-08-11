#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/7/22 10:28
# @Author    :Raink
from selenium.webdriver.common.by import By

from pytest_app.page.AddresList_page import AddresList
from pytest_app.page.App_base import BasePage


class Main(BasePage):

    def goto_message(self):
        pass

    # 添加成员
    def goto_addresslist(self):
        self.find(By.XPATH, '//*[@text="通讯录"]').click()
        self.find(By.XPATH, '//*[@text="添加成员"]').click()
        return AddresList(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass

    # 删除成员
    def del_add_Contac(self, value):
        self.find(By.XPATH, '//*[@text="通讯录"]').click()
        elements = self._driver.find_elements(By.XPATH, '//*[@class="android.widget.TextView"]')
        # 使用循环得到每一页的title 也就是姓名的数据
        for element in elements:  # 使用判断 如果获取元素组中有传进来的那个元素 直接返回True
            if value == element.get_attribute("text"):
                element.click()
                self.find(By.ID, 'com.tencent.wework:id/hcg').click()
                self.find(By.XPATH, "//*[@text='编辑成员']").click()
                self.find(By.XPATH, "//*[@text='删除成员']").click()
                self.find(By.ID, "com.tencent.wework:id/bga").click()
                return True
