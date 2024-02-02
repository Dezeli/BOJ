# 웜홀
import sys
input = sys.stdin.readline

def belmanford(start):
    min_time[start] = 0
    for i in range(1, N+1):
        for s in range(1, N+1):
            for next, T in graph[s]:
                if min_time[next] > min_time[s] + T:
                    min_time[next] = min_time[s] + T
                    if i == N:
                        return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    min_time = [10001 for _ in range(N+1)]
    
    for __ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    
    for __ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])

    cycle = belmanford(1)
    if not cycle:
        print("NO")
    else:
        print("YES")