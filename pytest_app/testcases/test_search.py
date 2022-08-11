#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_search.py
# @Time      :2022/7/19 17:08
# @Author    :Raink
from time import sleep

from selenium.webdriver.common.by import By

from pytest_app.testcases.base import Base


class TestWinxin(Base):

    def test_winxin(self):
        print("添加联系人")
        self.driver.find_element(By.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(By.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(By.XPATH,'//*[@class="android.widget.TextView" and @text="手动输入添加"]').click()
        self.driver.find_element(By.XPATH,'//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys("zhangsan")
        self.driver.find_element(By.XPATH,'//*[@text="性别"]/..//*[contains(@class,"TextView") and @text="男"]').click()
        self.driver.find_element(By.XPATH,'//*[@text="女"]').click()
        self.driver.find_element(By.XPATH,'//*[@text="手机　"]/..//*[contains(@class,"EditText")]').send_keys("13512341234")
        self.driver.find_element(By.ID,'com.tencent.wework:id/ad3').click()
        sleep(3)
        print(self.driver.page_source)
        test=self.driver.find_element(By.XPATH,"//*[@class='android.widget.Toast']").text
        assert "成功" in test



if __name__ == "__main__":
    run_code = 0
