# 로봇 청소기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def clean(r, c):
    global d

    if r<0 or r>N-1:
        return
    if c<0 or c>M-1:
        return

    room[r][c] = 2

    for _ in range(4):
        d -= 1
        d %= 4
        dy, dx = dir[d]
        if r+dy<0 or r+dy>N-1:
            continue
        if c+dx<0 or c+dx>M-1:
            continue
        if room[r+dy][c+dx] == 0:
            clean(r+dy, c+dx)
            return

    dy, dx = dir[d-2]
    if r+dy<0 or r+dy>N-1:
        return
    if c+dx<0 or c+dx>M-1:
        return
    if room[r+dy][c+dx] == 1:
        return
    clean(r+dy, c+dx)


clean(r, c)

cleaned = 0
for i in room:
    for j in i:
        if j==2:
            cleaned += 1

print(cleaned)