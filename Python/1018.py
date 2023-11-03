# 체스판 다시 칠하기

N, M = map(int, input().split())
min_change = 32
chess_board = []

color = 'W'
last_line_color = 'W'
for i in range(N):
    line = input()
    change_line = []
    for j in line:
        if j == color:
            change_line.append(0)
        else:
            change_line.append(1)
        if color == 'W':
            color = 'B'
        else:
            color = 'W'
    if last_line_color == 'W':
        color = 'B'
        last_line_color = 'B'
    else:
        color = 'W'
        last_line_color = 'W'
    chess_board.append(change_line)


def check(x, y):
    change = 0
    for i in range(8):
        change += sum(chess_board[x+i][y:y+8])
    return min([change, abs(change-64)])


for x1 in range(0, N-7):
    for y1 in range(0, M-7):
        cnt = check(x1, y1)
        min_change = min([min_change, cnt])

print(min_change)

