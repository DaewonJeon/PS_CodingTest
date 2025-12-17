while(True):
  try:
    num1, num2 = map(int, input().split())
    print(num1+num2)
  except EOFError:
    break

# 런타임 에러 발생은 
# 입력이 끝날 때(EOF) 정상적으로 빠져나와야 함
# 그렇지 않으면 input()에서 EOFError 발생 → 런타임 에러!
