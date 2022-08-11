#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :AddresList_page.py
# @Time      :2022/7/22 10:38
# @Author    :Raink
from pytest_app.page.App_base import BasePage
from pytest_app.page.MemberInvite_invit import MemberInvite


class AddresList(BasePage):

    def add_menber(self):
        return MemberInvite(self._driver)

if __name__ == "__main__":
    run_code = 0
