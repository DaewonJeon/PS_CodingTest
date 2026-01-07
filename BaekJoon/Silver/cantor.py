import sys

def cantor(n):
    if n == 0:
        return "-"
    
    prev = cantor(n - 1)
    space = " " * len(prev)
    return prev + space + prev


for line in sys.stdin:
    n = int(line.strip())
    print(cantor(n))
