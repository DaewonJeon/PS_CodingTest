import sys

# 21x21x21 크기의 3차원 리스트 초기화 (0부터 20까지 필요)
memo = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    # 1. 0 이하인 경우 (기저 사례)
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    # 2. 20을 초과하는 경우
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    # 3. 이미 계산된 값이 메모리에 있는 경우 바로 반환
    if memo[a][b][c] != 0:
        return memo[a][b][c]
    
    # 4. 문제의 조건에 따라 계산 및 메모이제이션
    if a < b and b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return memo[a][b][c]

# 입력 루프
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")