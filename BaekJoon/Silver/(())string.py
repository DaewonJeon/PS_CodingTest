import sys
input = sys.stdin.readline

n = int(input())

for i in range(0,n):  

    b = []
    x = input().strip()

    is_valid = True   # 체크해주는 변수

    for z in x:
        if z == '(':
            b.append(z)
        elif z == ')' and b:    # 리스트 b가 1개 이상 있다면, b는 True / pop() 은 맨 끝 인덱스 빼낸다
            b.pop()
        elif z == ')' and not b:  # not b 인덱스가 비워져있음, 리스트 b가 비어 있다면 >> b 자체는 False가 됩
            is_valid = False
            break
    
    if is_valid and not b:
        print("YES")
    else:
        print("NO")