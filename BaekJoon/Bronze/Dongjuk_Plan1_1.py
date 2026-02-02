import sys
input = sys.stdin.readline

# def fib(n): 
#     global count_1

#     if n == 1 or n == 2:
#         count_1 +=1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


def fibonacci(n):
    global count_2

    if n <= 2:
        return 1
    
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    
    for i in range(3, n + 1):
        count_2 +=1
        f[i] = f[i - 1] + f[i - 2] 
        
    return f[n]

# count_1 = 0
count_2 = 0

n = int(input())
# fib(n)

print(fibonacci(n) , count_2)