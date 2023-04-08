#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Solution
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
            