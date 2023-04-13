#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度

# 首先字符串长度1的情况
# 方法是首尾指针
# 需要注意首尾的场地
def lengthOfLongestSubstring(s):
    head = 0
    tail = 0
    if len(s)<2:
        return len(s)
    res = 1
    while tail<len(s)-1:
        tail += 1
        if s[tail] not in s[head:tail]:
            res = max(tail-head+1,res)
        else:
            while s[tail] in s[head:tail]:
                head +=1
    return res 
    