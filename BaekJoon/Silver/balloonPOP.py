import sys
from collections import deque  # 원형 구조, 회전 문제에서 deque 사용
input = sys.stdin.readline     # (풍선 번호, 이동 값) deque에 튜플로 함께 넣는다
                               # dq.rotate() 로 원형효과 
n = int(input())               # rotate(ㅁ)   ㅁ>0  오른쪽으로 민다 
x = list(map(int, input().split()))
dq = deque()

for i in range(n):
  dq.append((i+1, x[i]))

while dq:
  p, q = dq.popleft()
  print(p, end=" ")

  if not dq:
    break

  if q > 0:
    dq.rotate(-(q-1))
  else:
    dq.rotate(-q)