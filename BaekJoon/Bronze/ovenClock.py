h, m = map(int, input().split())
oven_time = int(input())

if oven_time + m >= 60:
    h += (oven_time + m) // 60
    m = (oven_time + m) % 60
else:
    m += oven_time

if h >= 24:
    h %= 24
print(h,m)