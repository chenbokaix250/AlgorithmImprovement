# 回文判断

str1 = "absbaa"

list1 = list(str1)

list_re = list1[::-1]

if list1 == list_re:
    print(True)
else:
    print(False)
