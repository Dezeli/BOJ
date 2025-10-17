# 타임머신
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = 10**5*N + 1

buses = [list(map(int, input().split())) for _ in range(M)]

min_times = [INF for _ in range(N+1)]
min_times[1] = 0

for _ in range(N-1):
    for A, B, C in buses:
        if min_times[A]==INF:
            continue
        min_times[B] = min(min_times[B], min_times[A]+C)

inf_check = min_times[:]
for A, B, C in buses:
    if inf_check[A]==INF:
        continue
    inf_check[B] = min(inf_check[B], inf_check[A]+C)

if inf_check==min_times:
    for i in range(2, N+1):
        if min_times[i]!=INF:
            print(min_times[i])
        else:
            print(-1)
else:
    print(-1)
