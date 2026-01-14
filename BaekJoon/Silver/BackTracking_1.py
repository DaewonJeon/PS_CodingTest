n,m = map(int, input().split())
result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):  # 방금 i = 1을 끝낸 상태( 1, 4 까지 했을때!!) 두번째 콜 마치고 이제서야 i=2 로간다  i = 2
        if i not in result:     # dfs for문 안에 { dfs for문{i=1,2,3,4  }>> i= 2시작 } 
            result.append(i) # 숫자 추가

            dfs() # 재귀 호출 (다음 깊이로)

            result.pop() # 돌아오면(백트래킹) 넣었던 숫자를 다시 빼줘야 함
                        # 마지막 1 4 경우에 i=4 로 반복종료 후 함수가 끝난다(리턴)
                        # 다시 dfs 로 복귀해서 바로 pop 실행한다 >> 빈 리스트됨
                    

dfs()