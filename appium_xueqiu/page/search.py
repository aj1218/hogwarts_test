#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :search.py
# @Time      :2022/8/4 11:57
# @Author    :Raink
from selenium.webdriver.common.by import By

from appium_xueqiu.page.App_base import BasePage


class Search(BasePage):
    def search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        self.find(By.XPATH, "//*[@text='BABA']").click()
        self.find(By.XPATH,
                  '//*[contains(@resource-id,"ll_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="加自选"]').click()

    def is_choose(self):  # 验证是否被选中
        eles = self.finds(By.XPATH,
                          '//*[contains(@resource-id,"ll_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="加自选"]')

        return len(eles) > 0  # 如果大于零说明已添加找到了 没有小于零说明没有找到


if __name__ == "__main__":
    run_code = 0
