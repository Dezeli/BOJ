# N과 M (2)
import sys

N, M = map(int, sys.stdin.readline().split(" "))
li = [0 for _ in range(M)]
visit = [False for _ in range(N)]


def DFS(N, M, D, S):
    if D == M:
        print(" ".join(str(i) for i in li))
        return

    for i in range(S, N):
        if not visit[i]:
            visit[i] = True
            li[D] = i + 1
            DFS(N, M, D + 1, i + 1)
            visit[i] = False


DFS(N, M, 0, 0)
