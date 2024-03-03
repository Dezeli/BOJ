# N-Queen
import sys
from copy import deepcopy

input = sys.stdin.readline
N = int(input())
board = [[""] * N for _ in range(N)]


def make_queen(line, board):
    if line == N:
        return 1

    cnt = 0
    for i in range(N):
        if not board[line][i]:
            dif = []
            board[line][i] = "Q"
            dif.append([line, i])
            l, r = i, i
            x_line = line
            while True:
                x_line += 1
                if x_line >= N:
                    break
                if l > 0:
                    l -= 1
                    if board[x_line][l] == "":
                        board[x_line][l] = "X"
                        dif.append([x_line, l])
                if r < N - 1:
                    r += 1
                    if board[x_line][r] == "":
                        board[x_line][r] = "X"
                        dif.append([x_line, r])
                if board[x_line][i] == "":
                    board[x_line][i] = "X"
                    dif.append([x_line, i])
            cnt += make_queen(line + 1, board)

            for j, k in dif:
                board[j][k] = ""
    return cnt


print(make_queen(0, board))
