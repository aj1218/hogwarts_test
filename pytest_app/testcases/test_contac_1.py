#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_contac_1.py
# @Time      :2022/7/22 11:57
# @Author    :Raink
from time import sleep

from pytest_app.page.app import *




class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        investpage = self.main.goto_addresslist().add_menber().addmenber_by_maunl().input_name().set_gender().input_phone().click_save()
        sleep(2)
        assert "成功" in investpage.get_toast()
        self.main.del_add_Contac("zhangsan")