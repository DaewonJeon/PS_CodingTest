n, m = map(int, input().split())

A = []
B = []

# 행렬A 입력
for _ in range(n):
    A.append(list(map(int, input().split())))

# 행렬B 입력
for _ in range(n):
    B.append(list(map(int, input().split())))

# 행렬 덧셈 출력
for i in range(n):
    for j in range(m):
        print(A[i][j] + B[i][j], end=" ")
    print()
