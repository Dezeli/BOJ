# 오목, 이길 수 있을까?
import sys

input = sys.stdin.readline

board = []

for i in range(10):
    board.append(list(input().rstrip()))


def ck_left(y, x):
    x_ck = 0
    if x > 0 and board[y][x - 1] == "X":
        x_ck += 1
        x_ck = x_ck + ck_left(y, x - 1)
    return x_ck


def ck_right(y, x):
    x_ck = 0
    if x < 9 and board[y][x + 1] == "X":
        x_ck += 1
        x_ck = x_ck + ck_right(y, x + 1)
    return x_ck


def ck_up(y, x):
    x_ck = 0
    if y > 0 and board[y - 1][x] == "X":
        x_ck += 1
        x_ck = x_ck + ck_up(y - 1, x)
    return x_ck


def ck_down(y, x):
    x_ck = 0
    if y < 9 and board[y + 1][x] == "X":
        x_ck += 1
        x_ck = x_ck + ck_down(y + 1, x)
    return x_ck


def ck_upleft(y, x):
    x_ck = 0
    if (y > 0 and x > 0) and board[y - 1][x - 1] == "X":
        x_ck += 1
        x_ck = x_ck + ck_upleft(y - 1, x - 1)
    return x_ck


def ck_upright(y, x):
    x_ck = 0
    if (y > 0 and x < 9) and board[y - 1][x + 1] == "X":
        x_ck += 1
        x_ck = x_ck + ck_upright(y - 1, x + 1)
    return x_ck


def ck_downleft(y, x):
    x_ck = 0
    if (y < 9 and x > 0) and board[y + 1][x - 1] == "X":
        x_ck += 1
        x_ck = x_ck + ck_downleft(y + 1, x - 1)
    return x_ck


def ck_downright(y, x):
    x_ck = 0
    if (y < 9 and x < 9) and board[y + 1][x + 1] == "X":
        x_ck += 1
        x_ck = x_ck + ck_downright(y + 1, x + 1)
    return x_ck


flag = False

for i in range(10):
    for j in range(10):
        if board[i][j] == ".":
            if ck_left(i, j) + ck_right(i, j) >= 4:
                print(1)
                flag = True
                break
            elif ck_up(i, j) + ck_down(i, j) >= 4:
                print(1)
                flag = True
                break
            elif ck_upleft(i, j) + ck_downright(i, j) >= 4:
                print(1)
                flag = True
                break
            elif ck_upright(i, j) + ck_downleft(i, j) >= 4:
                print(1)
                flag = True
                break
    if flag:
        break

if not flag:
    print(0)
