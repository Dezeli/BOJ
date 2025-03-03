# 네트워크 연결
import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


visit = [0 for _ in range(N+1)]

move = [[0, 1]]

cost = 0
while move:
    c, n = heapq.heappop(move)
    
    if visit[n]==1:
        continue
    visit[n] = 1
    cost += c

    for c1, n1 in graph[n]:
        heapq.heappush(move, [c1, n1])

print(cost)