# 치즈
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)


starts = [[0, 0]]
check_list = [[0]*M for _ in range(N)]
zero_check = [[False]*M for _ in range(N)]
num = 0

for i in range(M):
    check_list[0][i] += 1
    check_list[N-1][i] += 1

for i in range(N):
    check_list[i][0] += 1
    check_list[i][M-1] += 1


while True:
    if not starts:
        break
    new_start = []
    for start in starts:
        next = []
        y, x = start
        next += [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
        while next:
            y, x = next.pop()
            if y<0 or y>=N:
                continue
            if x<0 or x>=M:
                continue
            if paper[y][x] == 1:
                check_list[y][x] += 1
                if check_list[y][x] >= 2:
                    paper[y][x] = 0
                    zero_check[y][x] = True
                    new_start.append([y, x])
                continue
            else:
                if zero_check[y][x]:
                    continue
                else:
                    zero_check[y][x] = True
                    next += [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
    num += 1
    starts = [] + new_start

print(num-1)