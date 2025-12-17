n = int(input())
a = []

for i in range(0, n):
  x = int(input())
  if(x == 0):
    a.pop()
  else:
    a.append(x)
print(sum(a))