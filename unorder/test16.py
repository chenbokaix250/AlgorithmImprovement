#!/usr/bin/python3
# -*- coding: utf-8 -*-

def test(list,k):
    return list.count(k)


    

if __name__=="__main__":

    list = [1,2,3,3,3,3,4,5]
    # list = [1,3,4,5]
    k = 3
    res = test(list,k)
    print(res)