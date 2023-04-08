#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

# 给定一个 整数 n， 如果是完美数，返回 true；否则返回 false。

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #对于数字1:直接返回`False`
        if num == 1:
            return False
        #计数从1开始
        total = 1
        #我们只需要判断`2-int(sqrt(num))+1`的数，全部累加
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                #这里total要加上i和num // i
                total += (i + num // i)
        return total == num
    
# 最简单的方法是暴力解 看他的整除数 加在一起是否等于本身