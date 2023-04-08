#!/usr/bin/python3
# -*- coding: utf-8 -*-

lst=[]

for n in range(2,10001):
    s=0
    for i in range(1,n-1):
        if n%i == 0:
            s=s+i
    if s==n:
        lst.append(n)
print("list is: ",lst)