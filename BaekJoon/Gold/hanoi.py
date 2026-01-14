import sys

def hanoi(n, start, end, via):
    # 원판이 1개일 때는 그냥 옮기면 됨
    if n == 1:
        print(start, end)
        return

    # 1. N-1개의 원판을 start -> via 로 이동 (end를 거쳐서)
    hanoi(n - 1, start, via, end)

    # 2. 가장 큰 원판(N)을 start -> end 로 이동
    print(start, end)

    # 3. via에 있던 N-1개의 원판을 via -> end 로 이동 (start를 거쳐서)
    hanoi(n - 1, via, end, start)


n = int(sys.stdin.readline())

print(2**n - 1)   # 총 이동 횟수 출력 (2의 n제곱 - 1)

# 재귀 함수 실행 (n개의 원판을 1번 -> 3번으로 이동, 2번을 경유)
hanoi(n, 1, 3, 2)