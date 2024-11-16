# 벽 부수고 이동하기 3
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [input().rstrip() for _ in range(N)]


def inside(y, x):
    if y < 0 or y >= N:
        return False
    if x < 0 or x >= M:
        return False
    return True


def min_move():
    moveQ = deque()
    moveQ.append([0, 0, 0])
    cnt = [[[0] * (K + 1) for _ in range(M)] for __ in range(N)]
    min_b = [[11] * M for _ in range(N)]

    cnt[0][0][0] = 1
    min_b[0][0] = 0
    while moveQ:
        y, x, b = moveQ.popleft()
        if y == N - 1 and x == M - 1:
            return cnt[y][x][b]

        cur = cnt[y][x][b]

        nextQ = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
        for i, j in nextQ:
            if inside(i, j):
                if b != K and cur % 2 == 1:
                    if board[i][j] == "1" and (not min_b[i][j] <= b + 1):
                        cnt[i][j][b + 1] = cur + 1
                        min_b[i][j] = min(min_b[i][j], b + 1)
                        moveQ.append([i, j, b + 1])
                if board[i][j] == "0" and (not min_b[i][j] <= b):
                    cnt[i][j][b] = cur + 1
                    min_b[i][j] = min(min_b[i][j], b)
                    moveQ.append([i, j, b])
        if cur % 2 == 0:
            cnt[y][x][b] += 1
            moveQ.append([y, x, b])

    if not moveQ:
        return -1


print(min_move())
