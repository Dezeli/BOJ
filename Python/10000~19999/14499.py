# 주사위 굴리기
import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

d2 = [list(map(int, input().split())) for _ in range(N)]

dice = [0]*6 # 윗면0, 북1, 동2, 서3, 남4, 아랫면5

def move(dir):
    if dir==1:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif dir==2:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif dir==3:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif dir==4:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]


order = map(int, input().split())
for i in order:
    if i==1:
        if y+1>=M:
            continue
        y += 1
    elif i==2:
        if y-1<0:
            continue
        y -= 1
    elif i==3:
        if x-1<0:
            continue
        x -= 1
    elif i==4:
        if x+1>=N:
            continue
        x += 1
    move(i)    
    if d2[x][y]:
        dice[5] = d2[x][y]
        d2[x][y] = 0
    else:
        d2[x][y] = dice[5]
    print(dice[0])