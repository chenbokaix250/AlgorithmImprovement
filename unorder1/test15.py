#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 输入一个整数 n ，输出该数32位二进制表示中1的个数。其中负数用补码表示

# 与FFFF进行 & 运算 然后找出1的个数
# 个数查找用count方法
 
def test(n):
    return bin(n & 0xFFFFFFFF).count("1")


    

if __name__=="__main__":

    num = 10
    res = test(num)
    print(res)