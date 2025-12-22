import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    p = input().strip()

    if p.startswith("push"):
        i, x = p.split()
        queue.append(x)

    elif p == "pop":
        print(queue.popleft() if queue else -1)

    elif p == "size":
        print(len(queue))

    elif p == "empty":
        print(0 if queue else 1)

    elif p == "front":
        print(queue[0] if queue else -1)

    elif p == "back":
        print(queue[-1] if queue else -1)

# 큐 내용 정리 
# from collections import deque

# queue = deque()      # deque()>> 큐 문제의 자료구조

# queue.append(3)      # 뒤에 넣기
# queue.popleft()      # 앞에서 빼기

# 동작	코드
# push	queue.append(x)
# pop	queue.popleft()
# front	queue[0]
# back	queue[-1]

# startswith() > 해당 문자열로 시작하는지 봄
# 문자열.startswith("확인할문자")