#!/usr/bin/python3
# -*- coding: utf-8 -*-

def  singleNumber(nums):
        
    for i in nums:
        nums[0]^=nums[i]
    return nums[0];

print(singleNumber([2,3,2,1,1]))

