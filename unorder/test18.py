
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Python 2.7
 
def func(s):
    list1 = s.split()
    s = ' '.join(list1[::-1])
    return s 
print(func("I am a nowcoder."))

