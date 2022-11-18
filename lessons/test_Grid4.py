#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_Grid4.py
# @Time      :2022/10/23 15:36
# @Author    :Raink


from threading import Thread
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By


class GridTest():

    def test_baidu(self, driver):
        driver.get('https://testbyt.ininin.com/?v=22.10.175957#/login')
        driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys('15811112222')
        driver.find_element(By.CLASS_NAME, 'el-input').send_keys('123456')
        driver.find_element(By.CLASS_NAME, 'el-button login-btn el-button--primary').click()
    def node_driver(self, node):
        if node == "firefox":
            brother = DesiredCapabilities.FIREFOX.copy()
            driver = Remote(command_executor="http://localhost:4444", desired_capabilities=brother)
        elif node == "chrome":
            brother = DesiredCapabilities.CHROME.copy()
            driver = Remote(command_executor="http://localhost:4444", desired_capabilities=brother)
        driver.implicitly_wait(10)
        driver.maximize_window()
        self.test_baidu(driver)

    def runner(self):
        nodes_list = ['firefox', 'chrome']

        thread_list = []
        for browther in nodes_list:
            t = Thread(target=self.node_driver, args=(browther,))
            thread_list.append(t)

        for t in thread_list:
            t.start()

        for t in thread_list:
            t.join()


if __name__ == '__main__':
    GridTest().runner()

