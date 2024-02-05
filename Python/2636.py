# 치즈
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)


starts = [[0, 0], [0, M-1], [N-1, 0], [N-1, M-1]]
num = 0

cheese = 0
for line in paper:
    cheese += sum(line)
melt = 0

check_list = [[False]*M for _ in range(N)]
while True:
    cheese -= melt
    if not cheese:
        break

    melt = 0
    new_start = []
    for start in starts:
        next = [start]
        while next:
            y, x = next.pop()
            if y<0 or y>=N:
                continue
            if x<0 or x>=M:
                continue
            if check_list[y][x] and [y, x] != start:
                continue
            if paper[y][x] == 1:
                paper[y][x] = 0
                new_start.append([y, x])
                check_list[y][x] = True
                melt += 1
                continue
            next += [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
            check_list[y][x] = True
    num += 1
    starts = [] + new_start
print(num)
print(melt)