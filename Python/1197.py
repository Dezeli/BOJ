# 최소 스패닝 트리
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())

check = [0 for _ in range(V+1)]
line = [[0, 1]]
graph = defaultdict(list)
distance = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

while line:
    d, e = heapq.heappop(line)
    if sum(check)==V:
        break
    if check[e]==1:
        continue
    check[e] = 1
    distance += d
    for newd, newe in graph[e]:
        if check[newe]==1:
            continue
        heapq.heappush(line, [newd, newe])

print(distance)