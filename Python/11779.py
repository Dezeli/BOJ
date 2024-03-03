# 최소비용 구하기 2
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = 2e9

n = int(input())
m = int(input())

buses = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    buses[s].append([c, e])


start, end = map(int, input().split())

next_buses = []
min_cost = [INF for _ in range(n + 1)]
routes = [[] for _ in range(n + 1)]

heapq.heappush(next_buses, [0, [], start])
while next_buses:
    c, r, d = heapq.heappop(next_buses)

    if min_cost[d] < c:
        continue

    r.append(d)
    min_cost[d] = c
    if min_cost[d] == c:
        if 0 < len(routes[d]) <= len(r):
            continue
        else:
            routes[d] = [] + r
    else:
        routes[d] = [] + r
    for nextC, nextD in buses[d]:
        heapq.heappush(next_buses, [nextC + c, [] + r, nextD])

print(min_cost[end])
print(len(routes[end]))
print(*routes[end])
