#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_main.py
# @Time      :2022/7/26 14:59
# @Author    :Raink
import pytest
import yaml

from pytest_app.page_UI.app import App

testcase = yaml.safe_load(open(r"D:\pythonProject\hogwarts_test\pytest_app\page_UI\test_yaml.yaml"))
print(testcase)


class TestMain:
    def test_search(self):
        app = App()
        app.start().Main().goto_windows()

    @pytest.mark.parametrize("value1,value2", testcase)
    def test_main(self, value1, value2):
        print(value1)
        print(value2)
