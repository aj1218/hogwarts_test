#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :MemberInvite_invit.py
# @Time      :2022/7/22 10:45
# @Author    :Raink
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from pytest_app.page.App_base import BasePage
from pytest_app.page.contac_add import ContacAdd


class MemberInvite(BasePage):
    def addmenber_by_maunl(self):
        self.find(By.XPATH, '//*[@class="android.widget.TextView" and @text="手动输入添加"]').click()
        return ContacAdd(self._driver)

    def get_toast(self):
        sleep(2)
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
