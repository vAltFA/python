def fibo(n):
    if n <= 0:
        return 1
    else:
        return n * fibo(n-1) + fibo(n-2)

print(fibo(5))

