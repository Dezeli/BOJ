# 특정한 최단 경로
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
N, E = map(int, input().split(" "))
Graph = defaultdict(list)

for _ in range(E):
    u, v, d = map(int, input().split(" "))
    Graph[u].append([d, v])
    Graph[v].append([d, u])
v1, v2 = map(int, input().split(" "))


def short_move(start, final):
    short_distance = [sys.maxsize for _ in range(N + 1)]
    short_distance[start] = 0
    moves = [[0, start]]
    while moves:
        d, u = heapq.heappop(moves)
        for w, v in Graph[u]:
            if short_distance[v] > short_distance[u] + w:
                short_distance[v] = short_distance[u] + w
                heapq.heappush(moves, [short_distance[v], v])
    return short_distance[final]


route1 = short_move(1, v1) + short_move(v1, v2) + short_move(v2, N)
route2 = short_move(1, v2) + short_move(v2, v1) + short_move(v1, N)

if min([route1, route2]) < sys.maxsize:
    print(min([route1, route2]))
else:
    print(-1)
