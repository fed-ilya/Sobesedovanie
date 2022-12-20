def f(n,m):
    if n == m:
        return 1
    elif n < m:
        return 0
    else:
        return f(n - 1,m) + f(n // 3,m)
print(f(37,10)*f(10,2))