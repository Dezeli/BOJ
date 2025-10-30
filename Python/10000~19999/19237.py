# 어른 상어
import sys

input = sys.stdin.readline

N, M, k = map(int, input().split())

d2 = []
fish = [0]*(M+1)
alive = M
smell = [[[0, 0] for _ in range(N)] for __ in range(N)]
for i in range(N):
    d1 = list(map(int, input().split()))
    for j in range(N):
        if d1[j]:
            fish[d1[j]] = [i, j, 0]
            smell[i][j] = [k, d1[j]]
    d2.append(d1)


dx = [0, -1, 1, 0, 0] # 0 위1, 아래2, 왼3, 오4
dy = [1, 0, 0, -1, 1]

dir = [0]
start_dir = list(map(int, input().split()))
for i in range(1, M+1):
    fish[i][2] = start_dir[i-1]

for _ in range(M):
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    dir.append([0, up, down, left, right])

def update_smell(new_smell):
    for i, j, n in new_smell:
        smell[i][j] = [k+1, n]

    for i in range(N):
        for j in range(N):
            if smell[i][j][0] >= 1:
                smell[i][j][0] -= 1
            if smell[i][j][0] == 0:
                smell[i][j][1] = 0
    return 0

time_cnt = 0
while alive>1:
    new_smell = []
    time_cnt += 1
    if time_cnt > 1000:
        break
    for n in range(M, 0, -1):
        if not fish[n]:
            continue
        x, y, d = fish[n]
        fs = False
        for i in dir[n][d]:
            mx = x + dx[i]
            my = y + dy[i]
            if mx<0 or my<0 or mx>=N or my>=N:
                continue
            if smell[mx][my][0]==0:
                if d2[mx][my]!=0:
                    fish[d2[mx][my]] = 0
                    alive -= 1
                fx = mx
                fy = my
                fi = i
                break
            elif smell[mx][my][1]==n:
                if fs:
                    continue
                fx = mx
                fy = my
                fi = i
                fs = True
        d2[fx][fy] = n
        d2[x][y] = 0
        fish[n] = [fx, fy, fi]
        new_smell.append([fx, fy, n])
    update_smell(new_smell)

if time_cnt>1000:
    print(-1)
else:
    print(time_cnt)