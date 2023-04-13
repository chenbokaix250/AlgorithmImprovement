#!/usr/bin/python3
# -*- coding: utf-8 -*-

def replaceSpace(s):
    s_ = ''
    for j in s:
        if j == ' ':
            s_ = s_ + '%20'
        else:
            s_ = s_ + j
    return s_

result = replaceSpace("aa bb")

print(result)