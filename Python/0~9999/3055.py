# 탈출
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())

forest = [[i for i in input().rstrip()] for _ in range(R)]


def water(t, x, y):
    global R, C

    if x < 0 or y < 0:
        return
    if x >= C or y >= R:
        return

    if forest[y][x] == "*":
        if t > 0:
            return
        pass
    elif forest[y][x] == "D" or forest[y][x] == "S" or forest[y][x] == "X":
        return
    elif forest[y][x] == ".":
        forest[y][x] = t
    else:
        if forest[y][x] <= t:
            return
        else:
            forest[y][x] = t

    water(t + 1, x + 1, y)
    water(t + 1, x - 1, y)
    water(t + 1, x, y + 1)
    water(t + 1, x, y - 1)


for i in range(R):
    for j in range(C):
        if forest[i][j] == "*":
            water(0, j, i)
        elif forest[i][j] == "S":
            move = deque([[0, i, j]])


suc = False
visit = [[0] * C for _ in range(R)]
while move:
    t, i, j = move.popleft()
    if i < 0 or j < 0:
        continue
    if i >= R or j >= C:
        continue
    if visit[i][j] == 1:
        continue
    visit[i][j] = 1
    if forest[i][j] == "S" or forest[i][j] == ".":
        pass
    elif forest[i][j] == "D":
        suc = True
        break
    elif forest[i][j] == "X" or forest[i][j] == "*":
        continue
    else:
        if forest[i][j] <= t:
            continue

    move.append([t + 1, i + 1, j])
    move.append([t + 1, i - 1, j])
    move.append([t + 1, i, j + 1])
    move.append([t + 1, i, j - 1])

if suc:
    print(t)
else:
    print("KAKTUS")
