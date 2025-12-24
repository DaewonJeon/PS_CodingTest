from collections import deque

dq = deque()
n = int(input())

for i in range(1, n+1):
        dq.append(i)

while len(dq) > 1:
    dq.popleft()              # 1. 맨 위 카드 버리기
    dq.append(dq.popleft())   # 2. 다음 카드 뒤로 보내기

print(dq[0])