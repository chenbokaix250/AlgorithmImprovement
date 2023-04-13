#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 将所有0移至末尾

# 找到后 remove0 再append0

class Solution
    def moveZeros(nums):
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums
            