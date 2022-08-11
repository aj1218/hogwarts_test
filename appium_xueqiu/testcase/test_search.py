#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_search.py
# @Time      :2022/8/4 17:07
# @Author    :Raink
from appium_xueqiu.page.app import App


class TestSearch:

    def setup(self):
        self.seach=App().start().Main().goto_market().goto_search()

    def test_search(self):
        self.seach.search()
        # print(self.seach.is_choose())
        # assert self.seach.is_choose()





