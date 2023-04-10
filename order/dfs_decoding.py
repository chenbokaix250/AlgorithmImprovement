#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 给一个加密过的字符串解码，返回解码后的字符串。

# 加密方法是：k[c] ，表示中括号中的 c 字符串重复 k 次，例如 3[a] 解码结果是 aaa ，保证输入字符串符合规则。不会出现类似 3a , 3[3] 这样的输入。

# 利用递归 结束条件是 ]
# 数字: 乘
# [  : 递归
# ]  : 结束递归
def decodeString(str):
    def dfs(s,i):
        res,multi="",0
        while i<len(s):
            if '0' <= s[i] <= '9':
                multi = multi * 10 + int(s[i])
            elif s[i] == "[":
                i, tmp = dfs(s, i + 1)
                res += multi * tmp
                multi = 0
            elif s[i] == ']':
                return i,res 
            else:
                res += s[i]
            i += 1
        return res
    return dfs(s,0)

