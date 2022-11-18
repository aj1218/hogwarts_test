#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test__stack.py
# @Time      :2022/9/2 10:11
# @Author    :Raink
import inspect


def a():
    print(inspect.stack()[1].function)
    print("a")

def test_stack():
    a()



if __name__ == "__main__":
    run_code = 0
