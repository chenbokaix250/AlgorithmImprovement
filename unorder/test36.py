#!/usr/bin/python3
# -*- coding: utf-8 -*-

list = [1,3,5,6,7]

list1 = []
list2 = []

for i in list:
    if i%2 == 1:
        list1.append(i)
    else:
        list2.append(i)

# print(list1)
# print(list2)

res = list1 + list2

print(res)
    