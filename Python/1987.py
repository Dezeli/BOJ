# 알파벳
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_move = 0
alps = set()

for _ in range(R):
    board.append(list(input().rstrip()))


def move(x, y, cnt):
    global max_move
    max_move = max(max_move, cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in alps:
            alps.add(board[nx][ny])
            move(nx, ny, cnt+1)
            alps.remove(board[nx][ny])

alps.add(board[0][0])
move(0, 0, 1)
print(max_move)


