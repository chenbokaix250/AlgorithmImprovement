#!/usr/bin/python3
# -*- coding: utf-8 -*-

def test(str):
    len_str = len(str)
    for i in range(len_str):
        count = 0
        for j in range(len_str):
            if str[j] == str[i]:
                count += 1
        if count == 1:
            return str[i]

if __name__=="__main__":
    res = test("google")
    print(res)