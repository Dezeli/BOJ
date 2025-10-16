# 경사로
import sys

input = sys.stdin.readline

N, L = map(int, input().split())

d2 = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    same_cnt = 1
    last_h = -1
    downuntil = -1
    for j in range(N):
        if j <= downuntil:
            continue
        h = line[j]
        if h==last_h:
            same_cnt += 1
        elif last_h==-1:
            last_h = h
            continue
        else:
            if h-last_h==1 and L<=same_cnt:
                same_cnt = 1
                last_h = h
                continue
            elif h-last_h==-1:
                for c in range(j+1, j+L):
                    if c>N-1:
                        return 0
                    if line[c]!=h:
                        return 0
                downuntil = j+L-1
                same_cnt = 0
                last_h = h
                continue
            return 0
    return 1

row = [check(r) for r in d2]
col = [check(list(c)) for c in zip(*d2)]
# print(row, col)
print(sum(row+col))