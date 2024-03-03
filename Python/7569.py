# 토마토
from sys import stdin

M, N, H = map(int, stdin.readline().split(" "))

origin_map = []
new_map = [0 for _ in range(M * N * H)]
queue = []

for y in range(N * H):
    line = list(map(int, stdin.readline().split(" ")))
    origin_map.append(line)
    for x in range(M):
        if origin_map[y][x] == 1:
            queue.append([x, y])
        elif origin_map[y][x] == -1:
            new_map[y * M + x] = 1

time = -2
while queue:
    next = []
    for _ in range(len(queue)):
        x, y = queue.pop()
        if x < 0 or x >= M:
            continue
        if y < 0 or y >= N * H:
            continue
        if new_map[y * M + x] == 1:
            continue
        else:
            new_map[y * M + x] = 1
            if y % N == N - 1 and y % N == 0:
                next += [[x + 1, y], [x - 1, y], [x, y + N], [x, y - N]]
            elif y % N == N - 1:
                next += [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + N], [x, y - N]]
            elif y % N == 0:
                next += [[x + 1, y], [x - 1, y], [x, y + 1], [x, y + N], [x, y - N]]
            else:
                next += [
                    [x + 1, y],
                    [x - 1, y],
                    [x, y + 1],
                    [x, y - 1],
                    [x, y + N],
                    [x, y - N],
                ]
    queue += next
    time += 1

if sum(new_map) == M * N * H:
    print(time)
else:
    print(-1)
