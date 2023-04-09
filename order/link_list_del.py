#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 删除有序链表中的重复元素
# 使用指针遍历 判定当前节点和下个节点是否相同，相同则重新链接next（删除），不同则移动指针
import sys 

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = next 

class Solution(object):
    def delete(self,head):
        if head is None or head.next is None:
            return head 
        cur,next = head,head.next 
        while next:
            if next.val!=cur.val:
                cur = cur.next
            else:
                cur.next = next.next 
            next = next.next 
        return head 
