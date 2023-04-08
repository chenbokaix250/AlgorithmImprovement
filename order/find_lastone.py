#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2023/4/9 00:16
@Author  : chenbokai
@File    : find_lastone.py
'''

# 每隔两个数删除一个数 求最后剩下的
def find_lastone(list):
    while 1:
        pop1 = list.pop(0)
        pop2 = list.pop(0)
        if len(list) > 0:
            list.remove(list[0])
        else:
            list.append(pop2)
            break
        list.append(pop1)
        list.append(pop2)

    res = list[0]
    print(res)




if __name__ == '__main__':
    list1 = [0,1,2,3,4,5,6,7]
    find_lastone(list1)
    #print(res)


