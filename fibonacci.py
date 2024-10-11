def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        f, s = 0, 1
        for _ in range(2, n + 1):
            f, s = s, f + s
        return s

n = 12
resultado = fibonacci(n)
print(f"El termino {n} de Fibonacci es: {resultado}")
