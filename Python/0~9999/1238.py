# 파티
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M, X = map(int, input().split())

roads = defaultdict(list)

for _ in range(M):
    S, E, T = map(int, input().split())
    roads[S].append([T, E])


INF = 10**6


def move(Start):
    des = [[0, Start]]

    min_time = [INF for _ in range(N + 1)]
    while des:
        T, E = heapq.heappop(des)
        if min_time[E] <= T:
            continue
        min_time[E] = T

        for nextT, nextE in roads[E]:
            heapq.heappush(des, [nextT + T, nextE])

    if Start == X:
        return min_time
    else:
        return min_time[X]


time = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    if i == X:
        back = move(i)
        for j in range(len(back)):
            time[j] += back[j]
    else:
        time[i] += move(i)
time[0] = 0
print(max(time))
