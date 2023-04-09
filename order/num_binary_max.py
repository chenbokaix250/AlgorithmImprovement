#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 有一个二进制字符串num，可以选择该串中的任意一段区间进行取反(可以进行一次或不进行)，取反指将0变为1，将1变为0。那么取反之后的num可能的最大的字典序是多少呢。如有num=1000，取反变为1111是字典序最大的。

# 例子给的不好 理解成了随意反转 

# 牛客的描述好一些
# https://www.nowcoder.com/questionTerminal/4ca47baf4d5f4417afc0f99d6efc7d42?orderByHotValue=1&mutiTagIds=683&page=8&onlyReference=false

class Solution：
    def maxLexicographical(self , num ):
        c = []
        for i,a in enumerate(num):
            if a=='0':
                c.appemd(i)
            if c==[]:
                return num 
            i = 0
            j = 0
            while i<len(c)-1:
                if c[i]+1 == c[i+1]:
                    i += 1
                    j = c[i] + 1
                else:
                    j = c[i] + 1
                    break
            num = num[0:c[0]] + '1'*(i+1)+num[j:]
            return num 
            