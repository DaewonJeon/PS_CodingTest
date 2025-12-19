import sys
input = sys.stdin.readline

x=""                      # strip() >> 앞·뒤 공백, 탭, 개행 전부 제거
                          # rstrip() >> 오른쪽 공백만 제거
while True:               # rstrip('\n') >> 오른쪽 개행만 제거

    x = input().rstrip('\n') # rstrip('\n') 오른쪽 개행 제거
    if x == ".":
        break   

    stack = []
    is_valid = True

    for i in x: 
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')':
            if not stack or stack[-1] == '[':
                is_valid = False
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                is_valid = False
                break
            else:
                stack.pop()

    if is_valid and not stack:
        print("yes")
    else:
        print("no")