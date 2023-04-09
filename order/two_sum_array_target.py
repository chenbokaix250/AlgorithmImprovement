#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 数组中找到两个数的和等于目标值
# 暴力搜索（注意结束条件）

class Solution:
    def twoSum(self,nums,target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return None
                if nums[i]+nums[j] == target:
                    return [i,j]

if __name__=="__main__":
    solution=Solution()
    print(solution.twoSum([2,7,11,15],9))
