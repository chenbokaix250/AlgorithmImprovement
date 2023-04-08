#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2023/4/9 00:48
@Author  : chenbokai
@File    : find_string_in_list.py
'''

# 稀疏数组搜索
# 双指针二分法
def find_string_in_list(liststr,find_str):
    print(find_str)
    length = len(liststr)
    first=0
    last = length - 1

    while last >=first:
        mid = first + (last-first)//2
        if liststr[mid] == find_str:
            return mid
        elif liststr[mid] > find_str:
            last = mid-1
        else:
            first = first + 1
    return -1


if __name__ == '__main__':
    liststr= ["at","","","","ball","","","car","","","dad","",""]
    findstr = "ball"
    mid = find_string_in_list(liststr,findstr)

    print(mid)