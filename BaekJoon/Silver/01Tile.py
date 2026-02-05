import sys
input = sys.stdin.readline

def fibonacci(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    prevbb = 1
    prevb = 2

    for i in range(3, n + 1):
        current = (prevb + prevbb) % 15746
        # 다음 단계를 위해 값 교체
        prevbb = prevb
        prevb = current
        
    return prevb

n = int(input())
print(fibonacci(n))