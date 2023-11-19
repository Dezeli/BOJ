# 테트로미노
import sys

N, M = map(int, sys.stdin.readline().split())

Paper = []


for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    Paper.append(line)


directions = [('L', -1, 0), ('R', 1, 0), ('U', 0, -1), ('D', 0, 1)]
reverse_Dirs = {'L':'R', 'R':'L', 'U':'D', 'D':'U'}


sum_list = []

def add(shape, sum_num, cnt, x, y):
    if x>=M or x<0:
        return
    if y>=N or y<0:
        return
    
    sum_num += Paper[y][x]
    cnt += 1
    if cnt == 4:
        sum_list.append(sum_num)
        return
    
    rev_dir = reverse_Dirs[shape[-1]]
    if cnt == 2:
        if shape=='R':
            if x+1<M:
                add(shape, sum_num + Paper[y][x+1], 3, x, y-1)
                add(shape, sum_num + Paper[y][x+1], 3, x, y+1)
        elif shape=='D':
            if y+1<N:
                add(shape, sum_num + Paper[y+1][x], 3, x-1, y)
                add(shape, sum_num + Paper[y+1][x], 3, x+1, y)


    for dir, xp, yp in directions:
        if dir==rev_dir:
            continue

        add(shape+dir, sum_num, cnt, x + xp, y + yp)


for i in range(M):
    for j in range(N):
        add('R', Paper[j][i], 1, i+1, j)
        add('D', Paper[j][i], 1, i, j+1)
        add('L', Paper[j][i], 1, i-1, j)
        add('U', Paper[j][i], 1, i, j-1)

print(max(sum_list))