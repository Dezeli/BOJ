# 동굴
import sys
from collections import deque

input = sys.stdin.readline

N, M, C = map(int, input().split())
Sr, Sc = map(int, input().split())

cave = []

for _ in range(N):
    l = list(map(int, input().split()))
    cave.append(l)

move = deque([[0, Sr-1, Sc-1]])
visit = [[0]*M for _ in range(N)]

rupi = [0 for _ in range(10**6)]

while move:
    l, x, y = move.popleft()
    if x<0 or x>N-1:
        continue
    if y<0 or y>M-1:
        continue
    if visit[x][y]==1:
        continue
    visit[x][y] = 1
    if cave[x][y]==-1:
        continue

    rupi[l] += cave[x][y]
    move.append([l+1, x+1, y])
    move.append([l+1, x-1, y])
    move.append([l+1, x, y+1])
    move.append([l+1, x, y-1])

max_rupi = 0
cur_rupi = C
for i in range(l+1):
    cur_rupi += rupi[i]-C
    max_rupi = max(cur_rupi, max_rupi)

print(max_rupi)