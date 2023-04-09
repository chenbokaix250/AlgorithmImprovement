
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Python 2.7

# 按照单词进行reverse
# splite 将str放入数组 然后resverse 再装进str
# 装进数组的方式："".join(list)

def func(s):
    list1 = s.split()
    s = ' '.join(list1[::-1])
    return s 
print(func("I am a nowcoder."))

