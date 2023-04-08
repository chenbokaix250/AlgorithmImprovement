# 删除公共字符串

def delet_public_string(str1,str2):
    ans = []
    ld1 = list(str1)
    ld2 = list(str2)

    for i in ld1:
        if i not in ld2:
            ans.append(i)
    res = ''.join(ans)
    return res


if __name__ == '__main__':
    str1  = 'They are students.'
    str2 = 'aeiou'
    res = delet_public_string(str1,str2)
    print(res)


