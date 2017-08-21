#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "stay_sun"


with open('user.txt', 'r', encoding='utf-8') as f:
    """读取文件 根据空格分割取出行   然后在根据， 取出列的数据"""
    data = f.read()
    for line in data.split():
        user_li = line.split(",")
        user = user_li[0]
        user_email = user_li[1]
        print("user: %s email %s " % (user,user_email))

with open("scpit.txt", mode='a', encoding='utf-8') as f:
    """将字符串增加到文件"""
    f.write("aaa")