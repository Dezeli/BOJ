# 최단경로
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split(" "))
K = int(input())

Graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split(" "))
    Graph[u].append([w, v])

def short_distance(start):
    dis = [sys.maxsize for _ in range(V+1)]
    dis[start] = 0
    moves = [[0, start]]
    while moves:
        d, u = heapq.heappop(moves)
        for w, v in Graph[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(moves, [dis[v], v])

    return dis[1:]


for i in short_distance(K):
    if i < sys.maxsize:
        print(i)
    else:
        print("INF")