#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 输入一个长度为n整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

# 分治法

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
    