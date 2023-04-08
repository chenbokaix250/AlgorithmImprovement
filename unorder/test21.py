#-*- coding:utf-8 -*-

class Solution(object):
    def compressString(self,S):
        res = ""
        numlist = [0]*len(S)
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