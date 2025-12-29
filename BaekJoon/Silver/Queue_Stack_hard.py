from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))

# 큐인 자료구조들의 초기값만, 역순으로 저장
dq = deque()
for i in range(n):
    if a[i] == 0:          # 큐
        dq.appendleft(b[i])

# 입력값 처리
for x in c:
    dq.append(x)           # 뒤에 입력
    print(dq.popleft(), end=" ")
