#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Solution
    def moveZeros(nums):
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums
            