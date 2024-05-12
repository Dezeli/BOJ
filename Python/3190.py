# 뱀
import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
board = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(0, N + 2):
    board[0][i] = 1
    board[i][0] = 1
    board[i][N + 1] = 1
    board[N + 1][i] = 1

snake = deque([[1, 1]])
board[1][1] = 1

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y][x] = 2

dir = deque([[0, 1], [-1, 0], [0, -1], [1, 0]])
L = int(input())
change = []
for _ in range(L):
    t, d = input().rstrip().split()
    change.append([int(t), d])
change.append([-1, 0])

time = 0
dir_i = 0
while True:
    if change[dir_i][0] == time:
        if change[dir_i][1] == "L":
            dir.append(dir.popleft())
        else:
            dir.appendleft(dir.pop())
        dir_i += 1
    time += 1
    head = [snake[0][0] + dir[0][0], snake[0][1] + dir[0][1]]
    snake.appendleft(head)
    if board[head[0]][head[1]] == 1:
        break
    elif board[head[0]][head[1]] == 0:
        tail_y, tail_x = snake.pop()
        board[tail_y][tail_x] = 0
    board[head[0]][head[1]] = 1
print(time)
