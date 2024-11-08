# 로하의 농사
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(N)]
x, y, p = map(int, input().split())

visit = [[0] * M for _ in range(N)]

max_water = 0


def dps(x, y, p, d, w):
    global max_water

    if p == 0:
        max_water = max(max_water, w)
        return


dps(x, y, p, 0)
print(max_water)
