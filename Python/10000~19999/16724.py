# 피리 부는 사나이
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]

visit = [[0] * M for _ in range(N)]
safe = 0

for i in range(N):
    for j in range(M):
        if visit[i][j] == 1:
            continue
        cur = []
        nexti, nextj = i, j

        while True:
            next = board[nexti][nextj]
            visit[nexti][nextj] = -1
            cur.append([nexti, nextj])
            if next == "U":
                nexti -= 1
            elif next == "D":
                nexti += 1
            elif next == "L":
                nextj -= 1
            elif next == "R":
                nextj += 1

            if visit[nexti][nextj] == 1:
                break
            elif visit[nexti][nextj] == -1:
                safe += 1
                break

        for a, b in cur:
            visit[a][b] = 1

print(safe)
