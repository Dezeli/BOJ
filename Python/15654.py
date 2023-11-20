# N과 M (5)
import sys

N, M = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
nums.sort()
li = [0 for _ in range(M)]
visit = [False for _ in range(N)]

def DFS(N, M, D):
    if D==M:
        print(' '.join(str(nums[i-1]) for i in li))
        return
    
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            li[D] = i+1
            DFS(N, M, D+1)
            visit[i] = False

DFS(N, M, 0)