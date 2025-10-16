# 알고스팟
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

d2 = [[int(i) for i in input().rstrip()] for _ in range(N)]


visit = [[N*M]*M for _ in range(N)]

move = deque([[0, 0, 0]])

while move:
    x, y, b = move.popleft()
    if x<0 or x>=N or y<0 or y>=M:
        continue
    
    i = d2[x][y]
    if visit[x][y] > b:
        visit[x][y] = b
        move.append([x+1, y, b+i])
        move.append([x-1, y, b+i])
        move.append([x, y+1, b+i])
        move.append([x, y-1, b+i])

print(visit[N-1][M-1])
