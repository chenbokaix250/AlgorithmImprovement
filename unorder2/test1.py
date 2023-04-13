#method 1

def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n-1)+climbStairs(n-2)

res = climbStairs(3)

print(res)

# method2

# f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了
def climbStairs2(n):
    a = b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

res = climbStairs2(3)

print(res)
