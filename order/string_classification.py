#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2023/4/9 01:00
@Author  : chenbokai
@File    : string_classification.py
'''

# 输入多个字符串 返回其分类
# 分类规则： A交换任意位置的两个字符，可以得到B

i= 0
N= int(input())

str_line = []

while True:
    word = input()
    str_line.append(word)
    i = i+1
    if i == N:
        break
for j in range(len(str_line)):
    str_line[j] = ''.join(sorted(str_line[j]))
print(len(set(str_line)))