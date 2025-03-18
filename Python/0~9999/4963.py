# 섬의 개수
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def cnt_land(x, y):
    global w, h
    if x < 0 or y < 0:
        return
    if x >= w or y >= h:
        return
    if visit[y][x] == 1:
        return
    if world[y][x] == 0:
        return
    visit[y][x] = 1

    cnt_land(x - 1, y - 1)
    cnt_land(x, y - 1)
    cnt_land(x + 1, y - 1)
    cnt_land(x - 1, y)
    cnt_land(x + 1, y)
    cnt_land(x - 1, y + 1)
    cnt_land(x, y + 1)
    cnt_land(x + 1, y + 1)


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    world = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(w):
        for j in range(h):
            if visit[j][i] == 1:
                continue
            if world[j][i] == 0:
                continue
            cnt_land(i, j)
            cnt += 1
    print(cnt)
