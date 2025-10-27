# 최종 순위
import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n = int(input())
    t = list(map(int, input().split()))

    graph = [[0]*(n+1) for _ in range(n+1)]
    cnt = [0 for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            graph[t[i]][t[j]] = 1
            cnt[t[i]] += 1

    m = int(input())
    for __ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = 0
            graph[b][a] = 1
            cnt[a] -= 1
            cnt[b] += 1
        else:
            graph[b][a] = 0
            graph[a][b] = 1
            cnt[b] -= 1
            cnt[a] += 1

    ranks = []
    queue = []
    for i in range(1, n+1):
        if cnt[i]==0:
            queue.append(i)
    for __ in range(n):
        if len(queue)==0:
            print("IMPOSSIBLE")
            break
        elif len(queue)==1:
            c = queue.pop()
            ranks.append(c)
            for i in range(1, n+1):
                if graph[i][c]:
                    graph[i][c] = 0
                    cnt[i] -= 1
                    if cnt[i]==0:
                        queue.append(i)
        else:
            print("?")
            break
    if len(ranks)==n:
        print(*reversed(ranks))
