# 어린 왕자
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().rstrip())
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())

        if r > (abs(x1 - cx) ** 2 + abs(y1 - cy) ** 2) ** (1 / 2):
            cnt += 1
        if r > (abs(x2 - cx) ** 2 + abs(y2 - cy) ** 2) ** (1 / 2):
            cnt += 1
        if r > (abs(x1 - cx) ** 2 + abs(y1 - cy) ** 2) ** (1 / 2) and r > (
            abs(x2 - cx) ** 2 + abs(y2 - cy) ** 2
        ) ** (1 / 2):
            cnt -= 2
    print(cnt)
