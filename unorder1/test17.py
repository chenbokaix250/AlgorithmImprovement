#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ListNode to list 再reverse list [::-1]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
List=[]
while head:
    List.append(head.val)
    head = head.next 
ans =  List[::-1]

print(ans)
