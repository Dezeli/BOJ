# 도시 건설
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

road = defaultdict(list)
sum_cost = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append([c, b])
    road[b].append([c, a])
    sum_cost += c

visit = [0] * (N + 1)
visit[1] = 1
can_make = []
for r in road[1]:
    heapq.heappush(can_make, r)

while can_make:
    c, n = heapq.heappop(can_make)
    if visit[n] == 1:
        continue

    sum_cost -= c
    for cost, node in road[n]:
        if visit[node] == 0:
            heapq.heappush(can_make, [cost, node])
    visit[n] = 1

if sum(visit) == N:
    print(sum_cost)
else:
    print(-1)
