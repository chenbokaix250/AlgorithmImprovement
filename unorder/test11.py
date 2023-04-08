#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Solution:
    def reverse(self , x: int) -> int:
        # write code here
        if x==0:
            return 0
        if x>0:
            a = int(str(x)[::-1])
        else:
            # a = -int(str(-x)[::-1])
            a = -int(str(x)[1:][::-1])
        if a> 2**31 or a<-2**31:
            return 0
        else:
            return a
                   
s = Solution()
s = s.reverse(-1200)
print(s)
        