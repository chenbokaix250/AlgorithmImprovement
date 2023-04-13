#!/usr/bin/python3
# -*- coding: utf-8 -*-



def is_interleaving(a, b, c):
    n, m, k = len(a), len(b), len(c)
    if n + m != k:
        return False
    dp = [[False] * (m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] and a[i-1] == c[i-1]
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] and b[j-1] == c[j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = (dp[i-1][j] and a[i-1] == c[i+j-1]) or \
                       (dp[i][j-1] and b[j-1] == c[i+j-1])
    return dp[n][m]


print(is_interleaving("abc", "def", "adbecf"))