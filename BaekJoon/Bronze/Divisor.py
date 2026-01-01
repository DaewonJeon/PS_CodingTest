n= int(input())     #심화2 - 약수

x = list(map(int,input().split()))

if min(x) % 2 == 0 or max(x) % 2 == 0:
    print(max(x) * 2)
else:
    print(min(x) * max(x))
