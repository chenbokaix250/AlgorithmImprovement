# 给定一个长度为n的数组nums，数组由一些非负整数组成，现需要将他们进行排列并拼接，每个数不可拆分，使得最后的结果最大，返回值需要是string类型，否则可能会溢出。

# 暴力穷举 利用str加 避免int加

class Solution:
    def largestNumber(self, nums):
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int("".join(nums)))



ss = Solution()

a = [2,20,23,4,8]
res = ss.largestNumber(a)
print(res)