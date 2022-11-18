#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2022/9/2 15:58
# @Author    :Raink



import os
import shlex
import signal
import subprocess
from typing import List

import pytest

#
# @pytest.fixture(scope="class", autouse=True)
# def record():
#     cmd = shlex.split("scrcpy --record tmp.mp4")
#     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     yield
#     os.kill(p.pid, signal.CTRL_C_EVENT)