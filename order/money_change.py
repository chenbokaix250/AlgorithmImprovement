#!/usr/bin/python3
# -*- coding: utf-8 -*-

#输入金额后，能用，分割
import sys 

n = input("num:")

if n:
   n = int(n)
   fom = format(n,",")
   print(fom)

# python format

# 关于金额的问题
# https://blog.csdn.net/weixin_37989267/article/details/107664011