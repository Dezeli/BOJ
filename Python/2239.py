# 스도쿠


def row_check(r, num):
    for x in range(9):
        if num == board[r][x]:
            return False
    return True


def col_check(c, num):
    for x in range(9):
        if num == board[x][c]:
            return False
    return True


def box_check(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if board[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth):
    if depth >= len(zeros):
        for k in range(9):
            print("".join(map(str, board[k])))
        exit()

    nr, nc = zeros[depth]
    for j in range(1, 9 + 1):
        if row_check(nr, j) and col_check(nc, j) and box_check(nr, nc, j):
            board[nr][nc] = j
            dfs(depth + 1)
            board[nr][nc] = 0


board = []
zeros = []
for i in range(9):
    line = list(map(int, input()))
    for j in range(len(line)):
        if line[j] == 0:
            zeros.append((i, j))
    board.append(line)

dfs(0)
