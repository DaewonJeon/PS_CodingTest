from collections import Counter # 심화2 - 통계학
import sys
input = sys.stdin.readline

n=int(input())

list1 = []

for i in range(n):
    x = int(input())
    list1.append(x)
list1.sort()

x1 = sum(list1) / n

# 최빈값
cnt = Counter(list1)
max_freq = max(cnt.values())
modes = [k for k, v in cnt.items() if v == max_freq]
modes.sort()

if len(modes) == 1:
    mode = modes[0]
else:
    mode = modes[1]

print(f"{round(x1):.0f}")
print(list1[n//2])
print(mode)
print(list1[-1] - list1[0])
