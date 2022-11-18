#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_search.py
# @Time      :2022/8/4 17:07
# @Author    :Raink
import os
import sys

sys.path.append(os.path.abspath('%s/../..' % sys.path[0]))

import pytest
import yaml

from appium_xueqiu.page.app import App


class TestSearch():

    def setup(self):
        self.app = App()
        self.search = self.app.start().Main().goto_market().goto_search()

    @pytest.mark.parametrize("name", yaml.safe_load(
        open(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\search.yaml", encoding="UTF-8"))["name"])
    def test_search(self, name):
        self.search.search(name)
        if self.search.is_choose(name):
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)
