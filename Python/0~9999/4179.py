# 불!
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

d2 = []
fires = []
jihoon = []

for i in range(R):
    d1 = input().rstrip()
    for j in range(C):
        if d1[j]=='J':
            jihoon.append([i, j])
        elif d1[j]=='F':
            fires.append([i, j])
    d2.append(d1)

visit = [[0]*C for _ in range(R)]
time = 0
escape = False
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x, y in fires:
    visit[x][y] = 1

while jihoon:
    time += 1
    new_fires = []
    while fires:
        fx, fy = fires.pop()
        for i in range(4):
            nfx = fx + dx[i]
            nfy = fy + dy[i]
            if nfx<0 or nfy<0 or nfx>R-1 or nfy>C-1:
                continue
            if d2[nfx][nfy]!='#' and visit[nfx][nfy]==0:
                visit[nfx][nfy] = 1
                new_fires.append([nfx, nfy])
    new_jihoon = []
    while jihoon:
        jx, jy = jihoon.pop()
        if jx==0 or jy==0 or jx==R-1 or jy==C-1:
            escape = True
            break
        for i in range(4):
            njx = jx + dx[i]
            njy = jy + dy[i]
            if njx<0 or njy<0 or njx>R-1 or njy>C-1:
                continue
            if d2[njx][njy]!='#' and visit[njx][njy]==0:
                visit[njx][njy] = 1
                new_jihoon.append([njx, njy])
    if escape:
        break
    fires += new_fires
    jihoon += new_jihoon

if escape:
    print(time)
else:
    print("IMPOSSIBLE")