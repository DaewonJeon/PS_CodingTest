H, M = map(int, input().split())

if M - 45 < 0:
  if H -1 < 0:
    H = 23
    M = M + 15
  else:
    H = H - 1
    M = M + 15
else:
  M = M - 45
print(H, M)
