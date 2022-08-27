#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_yaml_load.py
# @Time      :2022/8/15 11:41
# @Author    :Raink
import yaml


def test_yaml_load():
    with open(r"D:\pythonProject\hogwarts_test\appium_xueqiu\page\main_yaml.yaml", encoding="utf-8") as f:
        steps = yaml.safe_load(f)["goto_market"]
        print(steps)
        for step in steps:
            if "by" in step.keys():
                print("查找元素")
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    print("click操作")
                if "send" == action:
                    value = step["value"]
                    print(f"send({value})")
