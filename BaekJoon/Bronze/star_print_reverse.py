star = int(input())

for i in range(0, star):
  for j in range(0, star):
    if j >= star-1-i:
      print("*", end="")
    else:
      print(" ", end="")
  print()