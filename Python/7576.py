# 토마토
from sys import stdin

M, N = map(int, stdin.readline().split(" "))

origin_map = []
new_map = [0 for _ in range(M*N)]
queue = []

for y in range(N):
    line = list(map(int, stdin.readline().split(" ")))
    origin_map.append(line)
    for x in range(M):
        if origin_map[y][x]==1:
            queue.append([x, y])
        elif origin_map[y][x]==-1:
            new_map[y*M+x] = 1

time = -2
while queue:
    next = []
    for _ in range(len(queue)):
        x, y = queue.pop()
        if x<0 or x>=M:
            continue
        if y<0 or y>=N:
            continue
        if new_map[y*M+x]==1:
            continue
        else:
            new_map[y*M+x] = 1
            next += [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    queue += next
    time += 1

if sum(new_map)==M*N:
    print(time)
else:
    print(-1)