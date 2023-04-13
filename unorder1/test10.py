#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 找到数组的共有前缀

# zip（拉链函数）函数会将每一位取出 
# 利用set去重 如果剩下一位 则说明是公有前缀

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
    
ss = Solution()
list1 = ["abca","abc","abca","abc","abcc"]
res = ss.longestCommonPrefix(list1)

print(res)