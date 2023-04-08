#!/usr/bin/python3
# -*- coding: utf-8 -*-

def test(list):
    lens = int(len(list)/2)
    return list[lens]
    

if __name__=="__main__":

    # list = [1,2,3,2,2,2,5,4,2]
    list = [3,3,3,3,2,2,2]
    res = test(list)
    print(res)