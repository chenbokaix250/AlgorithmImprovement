
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Python 2.7

# 将"Hello World"变形后就变成了"wORLD hELLO"

# swapcase方法用于大小写转换 其余的跟reseve word一致 
def func(s):
    list1 = s.split()
    s = ' '.join(list1[::-1])
    res = ''
    for letter in s:
        letter = letter.swapcase()
        res += letter
        res +=''
    return res[0:len(res)]
print(func("This is a sample"))

