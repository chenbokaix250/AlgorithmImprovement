# 利用python处理str的强大能力 
# 可以多次使用replace

class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 == 1):
            return False
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace("()","").replace("{}","").replace("[]","")
        if (s==""):
            return True
        else:
            return False