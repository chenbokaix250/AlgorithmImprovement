#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2023/4/9 01:07
@Author  : chenbokai
@File    : string_replace.py
'''

# 搜索到空格，替换为%100
# str不是深拷贝 需要赋值给另一个对象
str = input()

ss = str.replace(" ","%100")
print(ss)