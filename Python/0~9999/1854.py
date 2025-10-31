# K번째 최단경로 찾기
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])


visit = [[] for _ in range(n+1)]
heap = []
heapq.heappush(visit[1], 0)
heapq.heappush(heap, [0, 1])

while heap:
    c, b = heapq.heappop(heap)

    for dc, db in graph[b]:
        new_c = c+dc

        if len(visit[db]) < k:
            heapq.heappush(visit[db], -new_c)
            heapq.heappush(heap, [new_c, db])

        elif -visit[db][0] > new_c:
            heapq.heappop(visit[db])
            heapq.heappush(visit[db], -new_c)
            heapq.heappush(heap, [new_c, db])


for i in range(1, n+1):
    if len(visit[i])==k:
        print(-visit[i][0])
    else:
        print(-1)
