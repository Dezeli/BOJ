# 빙산
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def melt():
    for year in range(1, 1000000):
        iceSub = [[0] * M for _ in range(N)]
        for x in range(1, N - 1):
            for y in range(1, M - 1):
                if ice[x][y] > 0:
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if ice[nx][ny] == 0:
                            iceSub[x][y] += 1

        for x in range(1, N - 1):
            for y in range(1, M - 1):
                if ice[x][y] > 0:
                    ice[x][y] = max(0, ice[x][y] - iceSub[x][y])

        visited = [[False] * M for _ in range(N)]
        cnt = 0
        for x in range(1, N - 1):
            for y in range(1, M - 1):
                if ice[x][y] > 0 and not visited[x][y]:
                    BFS(x, y, visited)
                    cnt += 1
                    if cnt > 1:
                        return year

        if cnt == 0:
            return 0


def BFS(sx, sy, visited):
    queue = deque()
    queue.append([sx, sy])
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if ice[nx][ny] > 0 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True


print(melt())
