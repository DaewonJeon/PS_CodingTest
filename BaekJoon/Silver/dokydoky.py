n = int(input())
x = list(map(int, input().split()))

z = []        # 임시 공간/ 스택
need = 1      # 다음에 받아야 할 번호

for v in x:
    z.append(v)             # 일단 스택 공간으로 보냄

    # 스택 맨 위가 필요한 번호면 통과
    while z and z[-1] == need:
        z.pop()
        need += 1

# 모든 사람이 순서대로 나갔으면
if not z:
    print("Nice")
else:
    print("Sad")
