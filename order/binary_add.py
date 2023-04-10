# 给定两个用字符串表示的二进制数，返回他们的和。

# bin方法将num转化成二进制
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (bin(int(a,2)+int(b,2))[2:])
    
a = "1"
b = "3"

print(bin(int(b)+int(a))[2:])