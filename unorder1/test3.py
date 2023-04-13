#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
