#-*- coding:utf-8 -*-

# 利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2bc5a3。

# 设置res和sum 根据while i < len(S) - 1 and S[i] == S[i+1]的判断，处理sum 当跳出说明str中letter变化了 去更新res的值和出现个数

class Solution(object):
    def compressString(self,S):
        res = ""
        # numlist = [0]*len(S)
        i = 0
        while i < len(S):
            sum = 1
            while i < len(S) - 1 and S[i] == S[i+1]:
                sum += 1
                i += 1
            res += S[i]
            res += str(sum)
            i += 1
        if len(res)>=len(S):
            return S 
        else:
            return res 
        
ss = Solution()
input = "aabcccccaaa"

res = ss.compressString(input)
print(res)
