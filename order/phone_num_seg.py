#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 输入电话后，能用连接符分割
import sys 

n = input("num:")

if n:
    p_n  = str(n)
    result = p_n[0:3] + " " + p_n[3:7]+" "+p_n[7:11]
else:
    result = ''


print(result)


# 常规字符串切分