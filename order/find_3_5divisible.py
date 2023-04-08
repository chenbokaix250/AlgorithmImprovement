#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 找到能被3和5整除的数
import sys

n = int(input("num:"))

 
list = []
for i in range(1,n+1):
    if(i%(3*5)==0):
        list.append(i)
# print(list)
result = "3,5,"

for i in list:
    result = result + str(i) + ","
print(result)

# 需要str 所以用list进行了拼接
# 能被3和5整除 就是3,5 以及能被15整除