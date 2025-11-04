# 거의 최단 경로
import sys
import heapq

input = sys.stdin.readline

INF = 10**6

while True:
    N, M = map(int, input().split())
    if N==M==0:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((P, V))
    
    visit = [INF for i in range(N)]
    parents = [[] for i in range(N)]
    heap = []
    visit[S] = 0
    heapq.heappush(heap, (0, S))

    while heap:
        P, V = heapq.heappop(heap)
        if visit[V] < P:
            continue

        for dP, dV in graph[V]:
            if visit[dV] > dP + P:
                visit[dV] = dP + P
                parents[dV] = [V]
                heapq.heappush(heap, (dP+P, dV))
            elif visit[dV] == dP + P:
                parents[dV].append(V) 
    
    banned = [[0]*(N) for _ in range(N)]
    ban_queue = [D]
    ban_visit = [0 for _ in range(N)]
    while ban_queue:
        V = ban_queue.pop()
        if ban_visit[V]:
            continue
        ban_visit[V] = 1

        for U in parents[V]:
            banned[U][V] = 1
            ban_queue.append(U)

    
    visit = [INF for i in range(N)]
    heap = []
    visit[S] = 0
    heapq.heappush(heap, (0, S))

    while heap:
        P, V = heapq.heappop(heap)
        if visit[V] < P:
            continue

        for dP, dV in graph[V]:
            if banned[V][dV]:
                continue
            if visit[dV] > dP + P:
                visit[dV] = dP + P
                heapq.heappush(heap, (dP+P, dV))
    if visit[D]==INF:
        print(-1)
    else:
        print(visit[D])