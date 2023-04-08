#!/usr/bin/python3
# -*- coding: utf-8 -*-

def test(n):
    return bin(n & 0xFFFFFFFF).count("1")


    

if __name__=="__main__":

    num = 10
    res = test(num)
    print(res)