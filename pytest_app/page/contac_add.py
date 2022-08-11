#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :contac_add.py
# @Time      :2022/7/22 11:00
# @Author    :Raink
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from pytest_app.page.App_base import BasePage


class ContacAdd(BasePage):

    def input_name(self):
        self.find(By.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(
            "zhangsan")
        return self

    def set_gender(self):
        self.find(By.XPATH, '//*[@text="性别"]/..//*[contains(@class,"TextView") and @text="男"]').click()
        self.find(By.XPATH, '//*[@text="女"]').click()
        return self

    def input_phone(self):
        self.find(By.XPATH, '//*[@text="手机　"]/..//*[contains(@class,"EditText")]').send_keys(
            "13512341234")
        return self

    def click_save(self):  # 这个方案中的返回上一个页面的页面在首页点添加成员的时候会跳转添加成员的页面 然后在保存成员信息的时候
        # 保存成功之后页面也会跳转到添加成员的页面，如果把方法的导入写在上面就会出现重复调用的情况，所以需要把方法导入的引用写在类里面
        from pytest_app.page.MemberInvite_invit import MemberInvite
        # self.find(By.ID, 'com.tencent.wework:id/ad3').click()

        self.find(MobileBy.ID, "com.tencent.wework:id/ad3").click()
        sleep(1)
        self._driver.back()
        # return MemberInvite(self._driver)


