# 백조의 호수
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_melt(lake, visit, swans):
    next_swans = deque()
    while swans:
        x, y = swans.popleft()
        if x == melt[1][0] and y == melt[1][1]:
            return True, 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == False:
                visit[nx][ny] = True
                if lake[nx][ny] == "X":
                    next_swans.append((nx, ny))
                else:
                    swans.append((nx, ny))
    return False, next_swans


def change_melt(water, lake):
    new_water = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                lake[nx][ny] = "."
                new_water.append((nx, ny))
    return new_water


water = deque()
lake = []
melt = []
cnt = -1

for c in range(R):
    l = list(input().rstrip())
    for i, v in enumerate(l):
        if v == "L" or v == ".":
            water.append((c, i))
        if v == "L":
            melt.append((c, i))
    lake.append(l)

swans = deque()
swans.append((melt[0][0], melt[0][1]))
visit = [[False for _ in range(C)] for _ in range(R)]
visit[melt[0][0]][melt[0][1]] = True

while True:
    cnt += 1
    meet, next_swans = find_melt(lake, visit, swans)
    if meet:
        print(cnt)
        break
    water = change_melt(water, lake)
    swans = next_swans
