# 직사각형 탈출
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
p_sum = [[0 for _ in range(M+1)]]

for _ in range(N):
    l = list(map(int, input().split()))
    p = [0]
    for i in range(M):
        p.append(l[i] + p[-1] + p_sum[-1][i+1] - p_sum[-1][i])
    p_sum.append(p)

H, W, Sr, Sc, Fr, Fc = map(int, input().split())

move = [[-1]*(M+1) for _ in range(N+1)]
move[Sr][Sc] = 0
square = deque([[Sr, Sc]])
while square:
    r, c = square.popleft()
    if r-1 > 0 and move[r-1][c]==-1:
        x1, y1 = r-1, c
        x2, y2 = x1+H-1, y1+W-1
        check = p_sum[x2][y2]-p_sum[x1-1][y2]-p_sum[x2][y1-1]+p_sum[x1-1][y1-1]
        if check==0:
            move[x1][y1] = move[r][c] + 1
            square.append([x1, y1])
    if r+H < N+1 and move[r+1][c]==-1:
        x1, y1 = r+1, c
        x2, y2 = x1+H-1, y1+W-1
        check = p_sum[x2][y2]-p_sum[x1-1][y2]-p_sum[x2][y1-1]+p_sum[x1-1][y1-1]
        if check==0:
            move[x1][y1] = move[r][c] + 1
            square.append([x1, y1])
    if c-1 > 0 and move[r][c-1]==-1:
        x1, y1 = r, c-1
        x2, y2 = x1+H-1, y1+W-1
        check = p_sum[x2][y2]-p_sum[x1-1][y2]-p_sum[x2][y1-1]+p_sum[x1-1][y1-1]
        if check==0:
            move[x1][y1] = move[r][c] + 1
            square.append([x1, y1])
    if c+W < M+1 and move[r][c+1]==-1:
        x1, y1 = r, c+1
        x2, y2 = x1+H-1, y1+W-1
        check = p_sum[x2][y2]-p_sum[x1-1][y2]-p_sum[x2][y1-1]+p_sum[x1-1][y1-1]
        if check==0:
            move[x1][y1] = move[r][c] + 1
            square.append([x1, y1])

print(move[Fr][Fc])