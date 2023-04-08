#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
