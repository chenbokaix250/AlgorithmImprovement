#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 出现超过一般 list.sorted后 中间的肯定是
def test(list):
    lens = int(len(list)/2)
    return list[lens]
    

if __name__=="__main__":

    # list = [1,2,3,2,2,2,5,4,2]
    list = [3,3,3,3,2,2,2]
    res = test(list)
    print(res)