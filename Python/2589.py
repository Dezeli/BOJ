# 보물섬
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

tmap = [input().rstrip() for _ in range(N)]


def max_move(starti, startj):
    cnt = -1
    trace_map = [[0] * M for _ in range(N)]
    root = [[starti, startj]]
    next_root = []
    while True:
        while root:
            i, j = root.pop()
            if i < 0 or i >= N:
                continue
            if j < 0 or j >= M:
                continue
            if tmap[i][j] == "W":
                continue
            if trace_map[i][j] == 0:
                trace_map[i][j] = 1
                next_root += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]

        if next_root:
            cnt += 1
            root += next_root
            next_root = []
        else:
            break
    return cnt


max_time = -1

for i in range(N):
    for j in range(M):
        if tmap[i][j] == "W":
            continue
        max_time = max(max_time, max_move(i, j))

print(max_time)
