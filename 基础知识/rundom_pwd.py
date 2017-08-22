#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "stay_sun"
"""
获取随机字符串
"""
from random import choice
import string


def GenPassword(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


if __name__ == '__main__':
    for i in range(1,10):
        pwd=GenPassword(10)
        print(pwd)