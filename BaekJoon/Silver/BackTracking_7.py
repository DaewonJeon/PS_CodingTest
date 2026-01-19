import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -10**9
min_val = 10**9

def dfs(idx, current, p, m, t, d):
    global max_val, min_val
    
    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    
    if p > 0:
        dfs(idx + 1, current + nums[idx], p - 1, m, t, d)
    if m > 0:
        dfs(idx + 1, current - nums[idx], p, m - 1, t, d)
    if t > 0:
        dfs(idx + 1, current * nums[idx], p, m, t - 1, d)
    if d > 0:
        if current < 0:
            dfs(idx + 1, - (abs(current) // nums[idx]), p, m, t, d - 1)
        else:
            dfs(idx + 1, current // nums[idx], p, m, t, d - 1)

dfs(1, nums[0], plus, minus, mul, div)

print(max_val)
print(min_val)
