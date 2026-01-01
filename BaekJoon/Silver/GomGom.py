import sys             # 심화2 - 인사성 밝은 곰곰이 set()
input = sys.stdin.readline   # set - 중복없는 자료 (중복 X , 순서 X, 빠른 검색)
                             # set 비우기 - .clear() 리스트,세트,딕셔너리 모두 가능함 
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