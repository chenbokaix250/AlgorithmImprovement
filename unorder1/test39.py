#将字符串解析成可能的ip地址

# 通过三个点将字符串分为四段
# 三重循环来做，对于每一个可能的下标分割方式，判断每个字段是否成立：只有一位或前导位不是0，并且数组介于月0～255

class Solution:
    def restoreIpAddresses(self, s: str): #-> List[str]:
        res = []
        for i in range(1, len(s)-2):
            for j in range(i+1, len(s)-1):
                for k in range(j+1, len(s)):
                    fields = [s[:i], s[i:j], s[j:k], s[k:]]
                    if all([(len(field)==1 or field[0]!='0') and (int(field)>=0 and int(field)<=255) for field in fields]):
                        res.append(".".join(fields))
        return res


ss = Solution()

s = "25525511135"

res = ss.restoreIpAddresses(s)

print(res)