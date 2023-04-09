#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 反向字符串 使用list的切片 list[::-1]
import sys 

n = input("num:")

if n:
   n = str(n)
   r_n = n[::-1]
   print(r_n)
