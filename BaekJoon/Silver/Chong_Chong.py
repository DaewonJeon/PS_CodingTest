import sys
input = sys.stdin.readline

n=int(input())

z = set()


for i in range(n):
    x, y = input().split()
    
    if x == "ChongChong" or y =="ChongChong":
        z.add(x)
        z.add(y)

    elif x in z or y in z:
        z.add(x)
        z.add(y)
print(len(z))