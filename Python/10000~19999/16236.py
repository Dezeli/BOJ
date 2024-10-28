# 아기 상어
import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

space = []

for y in range(N):
    line = list(map(int, input().split()))
    for x in range(N):
        if line[x] == 9:
            startY, startX = y, x
            line[x] = 0
    space.append(line)


sum_time = 0
size = 2


def move(y, x):
    global sum_time, size

    check = [[False] * N for _ in range(N)]
    eat = False
    next_move = []
    heapq.heappush(next_move, [0, y, x])
    time = 0
    while next_move:
        t, y, x = heapq.heappop(next_move)
        if x < 0 or y < 0 or x >= N or y >= N:
            continue
        if space[y][x] > int(size):
            continue
        if 0 < space[y][x] < int(size):
            time = t
            eat = True
            space[y][x] = 0
            break
        if check[y][x]:
            continue

        check[y][x] = True
        heapq.heappush(next_move, [t + 1, y - 1, x])
        heapq.heappush(next_move, [t + 1, y, x - 1])
        heapq.heappush(next_move, [t + 1, y, x + 1])
        heapq.heappush(next_move, [t + 1, y + 1, x])

    sum_time += time
    size += 1 / int(size)
    if eat:
        move(y, x)


move(startY, startX)
print(sum_time)
