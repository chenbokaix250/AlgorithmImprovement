#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 分类排序 再组合

list = [6,6,5,6]
list6 = []
list5 = []
list4 = []
for i in list:
    if i == 4:
        list4.append(i)
    elif i==5:
        list5.append(i)
    elif i==6:
        list6.append(i)
    else:
        "some error!"

res = list6  + list4 + list5

print(res)