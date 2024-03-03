# N과 M (6)
import sys

N, M = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
nums.sort()
li = [0 for _ in range(M)]
visit = [False for _ in range(N)]


def DFS(N, M, Depth, Start):
    if Depth == M:
        print(" ".join(str(nums[i - 1]) for i in li))
        return

    for i in range(Start, N):
        li[Depth] = i + 1
        DFS(N, M, Depth + 1, i)


DFS(N, M, 0, 0)
