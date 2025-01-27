# 동방 프로젝트 (Small)
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

wall = [1 for _ in range(N)]
wall[0] = 0

for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x, y):
        wall[i] = 0
print(sum(wall) + 1)
