#!/usr/bin/python3
# -*- coding: utf-8 -*-

def ugly(n):
    res = [1]
    if n <=1 :
        return max(n,0)
    else:
        index2, index3, index5 = 0,0,0
        i = 0
        while i < n:
            i += 1
            res.append(min(res[index2]*2,res[index3]*3,res[index5]*5))
            if res[i] == res[index2]*2:
                index2 += 1
            if res[i] == res[index3]*3:
                index3 += 1
            if res[i] == res[index5]*5:
                index5 += 1
        return res[n-1]