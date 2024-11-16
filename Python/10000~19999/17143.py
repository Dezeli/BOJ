# 낚시왕
import sys

input = sys.stdin.readline


R, C, M = map(int, input().split())
cage = [[0 for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    cage[r - 1][c - 1] = (s, d - 1, z)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

fish_cnt = 0


def move():
    global cage
    next_cage = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if cage[i][j]:
                s, d, z = cage[i][j]
                nx = i + dx[d] * s
                ny = j + dy[d] * s
                while True:
                    if nx < 0:
                        nx = -nx
                        d = 1
                    elif nx >= R:
                        nx = 2 * R - nx - 2
                        d = 0
                    elif ny < 0:
                        ny = -ny
                        d = 2
                    elif ny >= C:
                        ny = 2 * C - ny - 2
                        d = 3
                    if 0 <= nx < R and 0 <= ny < C:
                        break
                if next_cage[nx][ny]:
                    if next_cage[nx][ny][2] < z:
                        next_cage[nx][ny] = (s, d, z)
                else:
                    next_cage[nx][ny] = (s, d, z)

    cage = next_cage


for p in range(C):
    for i in range(R):
        if cage[i][p]:
            fish_cnt += cage[i][p][2]
            cage[i][p] = (0, 0, 0)
            break
    move()

print(fish_cnt)
