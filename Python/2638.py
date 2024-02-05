# 치즈
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

four_dir = []
for i in range(N):
    line = []
    for j in range(M):
        noair = 4
        if i==0 or i==N-1:
            noair -= 1
        if j==0 or j==M-1:
            noair -= 1
        line.append(noair)
    four_dir.append(line)

starts = [[0, 0], [0, M-1], [N-1, 0], [N-1, M-1]]

num = 0
while True:
    cheese = 0
    for line in paper:
        cheese += sum(line)
    if not cheese:
        break 

    blank = []
    for start in starts:
        next = [start]
        while next:
            y, x = next.pop()
            if y<0 or y>=N:
                continue
            if x<0 or x>=M:
                continue
            four_dir[y][x] -= 1
            if [y, x] in blank:
                continue
            if paper[y][x] == 1:
                continue
            
            blank.append([y, x])
            next += [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
    
    for y in range(N):
        for x in range(M):
            if paper[y][x]==0 or four_dir[y][x]<=2:
                four_dir[y][x] = 0
                paper[y][x] = 0
            else:
                four_dir[y][x] = 4
    num += 1

print(num)