# N과 M (4)
import sys

N, M = map(int, sys.stdin.readline().split(" "))
li = [0 for _ in range(M)]


def DFS(N, M, Depth, Start):
    if Depth == M:
        print(" ".join(str(i) for i in li))
        return

    for i in range(Start, N):
        li[Depth] = i + 1
        DFS(N, M, Depth + 1, i)


DFS(N, M, 0, 0)
