# 미로 탐색
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

map = []
for _ in range(N):
    line = list(sys.stdin.readline().rstrip())
    map.append(line)


def find(N, M, root):
    queue = deque([root])

    while queue:
        x, y, cnt = queue.popleft()
        if x == M and y == N:
            return cnt
        if x < 0 or x > M:
            continue
        if y < 0 or y > N:
            continue
        if map[y][x] == "0":
            continue
        else:
            map[y][x] = "0"
            queue += [
                [x - 1, y, cnt + 1],
                [x + 1, y, cnt + 1],
                [x, y - 1, cnt + 1],
                [x, y + 1, cnt + 1],
            ]


print(find(N - 1, M - 1, [0, 0, 1]))
