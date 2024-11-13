# 대지

N = int(input())

max_x, max_y, min_x, min_y = -10000, -10000, 10000, 10000
for _ in range(N):
    x, y = map(int, input().split())
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    min_x = min(x, min_x)
    min_y = min(y, min_y)

print((max_x-min_x)*(max_y-min_y))