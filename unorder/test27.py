#!/usr/bin/python3
# -*- coding: utf-8 -*-


def formatString(Str,nums):
    num = int(Str.count("%s"))
    # print(num)
    arg1 = list(nums)
    # print(len(arg1))
    if num < len(arg1):
        for i in range(num):
            s=arg1[i]
            Str = Str.replace("%s",s,1)
        Str=Str+arg1[num]
        return Str 
    else:
        for i in range(num):
            s=arg1[i]
            Str = Str.replace("%s",s,1)
        return Str

res  = formatString("A%sC%sE",['B','D','F'])
print(res)

          
