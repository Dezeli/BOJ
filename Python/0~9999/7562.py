# 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    I = int(input())
    cur = list(map(int, input().split()))
    final = list(map(int, input().split()))

    visit = [[0] * I for _ in range(I)]

    move = deque([[0, cur[0], cur[1]]])

    while move:
        c, x, y = move.popleft()

        if x < 0 or y < 0:
            continue
        if x >= I or y >= I:
            continue
        if visit[x][y] == 1:
            continue
        visit[x][y] = 1

        if final == [x, y]:
            print(c)
            break

        move.append([c + 1, x - 1, y - 2])
        move.append([c + 1, x + 1, y - 2])
        move.append([c + 1, x - 2, y - 1])
        move.append([c + 1, x + 2, y - 1])
        move.append([c + 1, x - 2, y + 1])
        move.append([c + 1, x + 2, y + 1])
        move.append([c + 1, x - 1, y + 2])
        move.append([c + 1, x + 1, y + 2])
