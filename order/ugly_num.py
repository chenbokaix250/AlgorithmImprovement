#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。


# 暴力法
# 找出2*n 3*n 5*n，然后list合并去重 然后找到n-1的位置的值

# 法2：以2，3，5为基准，将丑数乘以他们三最小的且还没放入丑数中的作为丑数 用三个下标分别代表2，3，5现在对应的丑数列表中的下标

def ugly(n):
    res = [1]
    if n <=1 :
        return max(n,0)
    else:
        index2, index3, index5 = 0,0,0
        i = 0
        while i < n:
            i += 1
            res.append(min(res[index2]*2,res[index3]*3,res[index5]*5))
            if res[i] == res[index2]*2:
                index2 += 1
            if res[i] == res[index3]*3:
                index3 += 1
            if res[i] == res[index5]*5:
                index5 += 1
        return res[n-1]
# method 2
def ugly(n):
    nums = [i+1 for i in range(n)]
    # print(nums)
    num0 = [1]
    nums2 = [ j*2 for j in nums]
    # print(nums2)
    nums3 = [ k*3 for k in nums]
    nums5 = [ l*5 for l in nums]
    # print(nums3)
    # print(nums5)
    list1 = num0 + nums2 + nums3 + nums5

    list1.sort()

    # print(list1)
    list1 = list(set(list1))

    print(list1[n-1])
print(ugly(8))#9