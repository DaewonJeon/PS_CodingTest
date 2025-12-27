import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for i in range(0,n):
  x = input().strip()
  
  if x == "3":
    if dq:
      print(dq.popleft())
    else:
      print("-1")
  elif x == "4":
      if dq:
          print(dq.pop())  
      else:
          print("-1")
  elif x =="5":
      print(len(dq))
  elif x == "6":
      if dq:
          print("0")
      else:
          print("1")
  elif x == "7":
      if dq:
          print(dq[0])
      else:
          print("-1")
  elif x == "8":
      if dq:
          print(dq[-1])
      else:
          print("-1")


  if x.startswith("1 "):
      dq.appendleft(x.split()[1])
  elif x.startswith("2 "):
      dq.append(x.split()[1])

    
    

