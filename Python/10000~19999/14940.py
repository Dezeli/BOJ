# 쉬운 최단거리
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split(" "))

origin_map = []
for i in range(n):
    line = list(map(int, stdin.readline().split(" ")))
    origin_map.append(line)
    if 2 in line:
        start_x, start_y = line.index(2), i

queue = deque()
queue.append([start_x, start_y, 0])

dis_map = [[0 if origin_map[y][x] == 0 else -1 for x in range(m)] for y in range(n)]

while queue:
    x, y, num = queue.popleft()

    if x < 0 or x >= m:
        continue
    if y < 0 or y >= n:
        continue

    if origin_map[y][x] != 0:
        dis_map[y][x] = num
        origin_map[y][x] = 0
        queue.append([x + 1, y, num + 1])
        queue.append([x - 1, y, num + 1])
        queue.append([x, y + 1, num + 1])
        queue.append([x, y - 1, num + 1])

for line in dis_map:
    print(" ".join(str(i) for i in line))
