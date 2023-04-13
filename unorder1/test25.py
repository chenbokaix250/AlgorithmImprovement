#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 给只包含小写英文字母和数字的字符排序
# 利用字典遍历 得到字母和出现的数组 再组装到list中
# 利用list对key进行倒序排列
# 再通过str读出返回

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