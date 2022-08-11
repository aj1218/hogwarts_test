#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_wrapper.py
# @Time      :2022/8/10 10:52
# @Author    :Raink

def extend(fuc):
    def hello(*args, **kwargs):  # 接受任意参数 *args, **kwargs  包含字典，字符串 等所有的参数内类型
        print("hello")
        fuc(*args, **kwargs)
        print("good bye")

    return hello

@extend
def tmp():
    print("tmp")

@extend
def tmp1():
    print("tmp1")


def test_wrapper():
    # extend(tmp)()   # 不加@extend
    # extend(tmp1)() # 不加@extend

    tmp()  # 加 @extend
    tmp1()  # 加 @extend


