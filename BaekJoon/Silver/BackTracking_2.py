n,m = map(int, input().split())
result = []

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, n+1):
        if i not in result:
            result.append(i) # 숫자 추가

            dfs(i+1) # 재귀 호출 (다음 깊이로)

            result.pop() # 돌아오면(백트래킹) 넣었던 숫자를 다시 빼줘야 함


dfs(1)