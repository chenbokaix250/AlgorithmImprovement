#!/usr/bin/python3
# -*- coding: utf-8 -*-

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