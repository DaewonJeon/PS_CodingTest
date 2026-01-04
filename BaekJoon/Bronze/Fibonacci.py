def Fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input())
print(Fibonacci(n))