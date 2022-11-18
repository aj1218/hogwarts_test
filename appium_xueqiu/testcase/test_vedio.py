#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_vedio.py
# @Time      :2022/9/2 16:23
# @Author    :Raink

import os
import shlex
import signal
import subprocess
from time import sleep


def test_vedio():
    cmd = shlex.split("scrcpy --record tmp55.mp4")
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(p)
    sleep(10)
    os.kill(p.pid, signal.CTRL_C_EVENT)
