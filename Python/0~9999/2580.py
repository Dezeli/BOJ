# 스도쿠
import sys

input = sys.stdin.readline

sdoku = [list(map(int, input().split())) for _ in range(9)]
blanks = []

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blanks.append((i, j))


def checkRow(x, a):
    for i in range(9):
        if a == sdoku[x][i]:
            return False
    return True


def checkCol(y, a):
    for i in range(9):
        if a == sdoku[i][y]:
            return False
    return True


def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sdoku[nx + i][ny + j]:
                return False
    return True


def dfs(idx):
    if idx == len(blanks):
        for i in range(9):
            print(*sdoku[i])
        exit(0)

    for i in range(1, 10):
        x = blanks[idx][0]
        y = blanks[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            sdoku[x][y] = i
            dfs(idx + 1)
            sdoku[x][y] = 0


dfs(0)
