#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 字符去重

# 遍历时 使用xx not in xxx进行判定

# ss = input()
ss = "BAabB"

res_set = []

for i in ss:
    # print(i)
    if i not in res_set:
        res_set.append(i)
res = ''.join(res_set)
print(res_set)
print(res)