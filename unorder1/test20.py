#-*- coding:utf-8 -*-

# 有序数组的二分查找
# 处理lenth_low lenth_high与lenth_haf
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        lenth_low = 0
        lenth_high = len(nums)-1
        lenth_half = (lenth_low + lenth_high)//2
        while lenth_low<=lenth_high:
            lenth_haf=(lenth_low+lenth_high)//2
            if target==nums[lenth_haf]:
                return lenth_haf
            if target>nums[lenth_haf]:
                lenth_low=lenth_haf+1
                
            if target<nums[lenth_haf]:
                lenth_high=lenth_haf-1
        return -1


