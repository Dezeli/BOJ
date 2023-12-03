# N과 M (9)
import sys

N, M = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
nums.sort()
temp = []
visit = [False for _ in range(N)]


def DFS(N, M):
    if len(temp)==M:
        print(*temp)
        return
    
    same = 0
    for i in range(N):
        if not visit[i] and same != nums[i]:
            visit[i] = True
            temp.append(nums[i])
            same = nums[i]
            DFS(N, M)
            visit[i] = False
            temp.pop()

DFS(N, M)