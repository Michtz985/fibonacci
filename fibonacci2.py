def fibonacci(n, xd={}):
    if n in xd:
        return xd[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        xd[n] = fibonacci(n - 1, xd) + fibonacci(n - 2, xd)
        return xd[n]


n = 12 
for i in range(n):
    print(fibonacci(i))
