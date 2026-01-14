def draw_stars(n):
    # 1. 종료 조건 (Base Case)
    # n이 1이면 별 하나만 담긴 리스트를 반환
    if n == 1:
        return ['*']

    # 2. 재귀 호출
    # n/3 크기의 별 패턴을 먼저 구함 (이전 단계의 패턴을 가져옴)
    stars = draw_stars(n // 3)
    
    L = []  # 이번 단계에서 완성할 리스트

    # 3. 패턴 조립
    
    # [윗부분] : 작은 패턴 3개를 가로로 이어 붙임
    # 예: *** + *** + ***
    for s in stars:
        L.append(s * 3)
    
    # [중간부분] : 작은 패턴 + 공백 + 작은 패턴
    # 예: *** + (   ) + ***
    for s in stars:
        # 공백의 크기도 n/3 만큼이어야 함
        L.append(s + ' ' * (n // 3) + s)
    
    # [아랫부분] : 윗부분과 동일하게 3개 이어 붙임
    for s in stars:
        L.append(s * 3)
        
    return L

n = int(input())

# 결과 출력 (리스트의 각 줄을 개행문자로 합쳐서 출력)
print('\n'.join(draw_stars(n)))