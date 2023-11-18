# 테트로미노
import sys

N, M = map(int, sys.stdin.readline().split())

Paper = []


for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    Paper.append(line)



dir = [('L', -1, 0), ('R', 1, 0), ('U', 0, -1), ('D', 0, 1)]
reverse_Dirs = {'L':'R', 'R':'L', 'U':'D', 'D':'U'}
def add(before, sum_num, cnt, x, y):
    sum_num += Paper[y][x]
    cnt += 1
    if cnt == 4:
        print(before, sum_num)
        return
    
    rev_dir = reverse_Dirs[before[-1]]

    for s, xp, yp in dir:
        if s == rev_dir:
            continue
        add(before+s, sum_num, cnt, x+xp, y+yp)

add('R', 0, 0, 1, 1)