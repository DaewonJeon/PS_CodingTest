a=[]
for i in range(9):
  x = int(input())
  a.append(x)

print(max(a))
for j in range(9):
  if max(a) == a[j]:
    print(j+1)

# index()로도 쉽게 가능하다