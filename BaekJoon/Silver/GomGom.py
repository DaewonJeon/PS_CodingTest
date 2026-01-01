import sys             # 심화2 - 인사성 밝은 곰곰이 set()
input = sys.stdin.readline

n = int(input())
user = set()
count = 0

for x in range(n):
    s = input().strip()
    
    if s == "ENTER":
        user.clear()
    else:
        if s not in user:
            count += 1
            user.add(s)

print(count)