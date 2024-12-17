# Ignition
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

inf = 20000 + 1
d = [[inf]*(N+1) for _ in range(N+1)]
lines = []

for i in range(N+1):
    d[i][i] = 0

for _ in range(M):
    i, j, cost = map(int, input().split())
    d[i][j] = min([d[i][j], cost])
    d[j][i] = min([d[j][i], cost])
    lines.append([i, j, cost])

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])


max_times = [0]*(N+1)

for i, j, cost in lines:
    for c in range(1, N+1):
        b = max(d[c][i], d[c][j])
        s = min(d[c][i], d[c][j])
        extra = (cost-(b-s))/2
        max_times[c] = max(max_times[c], b+extra)

print(min(max_times[1:]))