# 준표의 조약돌
import sys

input = sys.stdin.readline

N, B, W = map(int, input().split())
road = input().rstrip()
l, r = 0, 0
max_len = 0

black = 0
white = 0
if road[0] == "W":
    white += 1
else:
    black += 1
if black <= B and white >= W:
    max_len = 1

while r + 1 < N:
    if black <= B:
        r += 1
        if road[r] == "W":
            white += 1
        else:
            black += 1
    else:
        if road[l] == "W":
            white -= 1
        else:
            black -= 1
        l += 1

    if black <= B and white >= W:
        max_len = max(r - l + 1, max_len)

print(max_len)
