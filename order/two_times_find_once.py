#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 给定一个整数数组，数组中有一个数出现了一次，其他数出现了两次，请找出只出现了一次的数。

# 考察异或运算
# 异或运算两个重要的性质：
# 1.x^x =0
# 2.x^0 =x
# 所以出现两次的经过异或都是0 最后剩下出现一次的

def  singleNumber(nums):
        
    for i in nums:
        nums[0]^=nums[i]
    return nums[0];

print(singleNumber([2,3,2,1,1]))

print(0^3)
