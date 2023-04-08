#!/usr/bin/python3
# -*- coding: utf-8 -*-

ss = input()
dic = {}
for x in ss:
    dic[x] = dic.get(x,0) + 1
print(dic)
list1 = []
for key,value in dic.items():
    list1.append([key,value])
print(list1)
list1.sort(key = lambda x:(-x[1],x[0]))
rlist = ''.join([i[0] for i in list1])
print(rlist)