from collections import deque # 어렵게 시도 후 풀이

n, k = map(int ,input().split())
stack = deque()
result = []

for i in range(1,n+1):
    stack.append(i)

while len(stack) != 0:

    for j in range(0, k-1):
        stack.append(stack.popleft())

    result.append(stack.popleft())

print(f"<{', '.join(map(str, result))}>")
