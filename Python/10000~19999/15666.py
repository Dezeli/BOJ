# N과 M (12)
import sys

N, M = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
nums.sort()
temp = []


def DFS(N, M):
    if len(temp) == M:
        print(*temp)
        return

    same = 0
    for i in range(N):
        if same != nums[i]:
            if temp:
                if temp[-1] > nums[i]:
                    continue
            temp.append(nums[i])
            same = nums[i]
            DFS(N, M)
            temp.pop()


DFS(N, M)
