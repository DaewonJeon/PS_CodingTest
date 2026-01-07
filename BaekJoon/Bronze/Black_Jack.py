import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x = list(map(int, input().split()))

alsum = 0

for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            kkk = x[i] + x[j] + x[z]
            if kkk <= m:
                alsum = max(alsum, kkk)

print(alsum)
