total = int(input())
num = int(input())

sum = 0
for i in range(0,num):
  price, quantity = map(int, input().split())

  sum += price * quantity

if sum == total:
  print("Yes")
else:
  print("No")