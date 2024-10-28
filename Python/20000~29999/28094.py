# 기말고사 작품 전시
import sys

input = sys.stdin.readline


def DFS(d, N, visited, cost):
    global ans, cnt
    if d == N:
        score = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if visited[i] < visited[j]:
                    score += cost[i][j]
        if score > ans:
            ans = score
            cnt = 1
        elif score == ans:
            cnt += 1
        return

    for i in range(1, len(visited)):
        if visited[i] == -1:
            visited[i] = d
            DFS(d + 1, N, visited, cost)
            visited[i] = -1


T = int(input())

for _ in range(T):
    ans = 0
    cnt = 0

    N, M = map(int, input().split())

    cost = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        V, A, B = map(int, input().split())
        cost[A][B] += V

    visited = [-1] * (N + 1)
    DFS(0, N, visited, cost)

    print(ans, cnt)
