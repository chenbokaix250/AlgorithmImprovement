#!/usr/bin/python3
# -*- coding: utf-8 -*-

list = [-2,3,4,1,5]

list.sort()

list1 = [i for i in list if i > 0]



# print(list1)

index = list1[0] 

ans=0
for i in list1:
    if index == i:
        index +=1
    else:
        ans = index
if ans == 0:
    ans = list1[-1] + 1
print(ans)


    