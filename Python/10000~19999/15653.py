# 구슬 탈출 4
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

visit = [[[[0]*M for _ in range(N)] for __ in range(M)] for ___ in range(N)]

board = []

for i in range(N):
    line = input().rstrip()
    for j in range(M):
        if line[j]=='R':
            R = [i, j]
            line = line.replace('R', '.')
        if line[j]=='B':
            B = [i, j]
            line = line.replace('B', '.')
    board.append(line)


def moveR(y, x):
    for i in range(x+1, M):
        m = board[y][i]
        if m=='O':
            return -1
        elif m=='#':
            return [y, i-1]

def moveL(y, x):
    for i in range(x-1, -1, -1):
        m = board[y][i]
        if m=='O':
            return -1
        elif m=='#':
            return [y, i+1]

def moveU(y, x):
    for i in range(y-1, -1, -1):
        m = board[i][x]
        if m=='O':
            return -1
        elif m=='#':
            return [i+1, x]

def moveD(y, x):
    for i in range(y+1, N):
        m = board[i][x]
        if m=='O':
            return -1
        elif m=='#':
            return [i-1, x]


cur = [[R, B]]
end = False
i = 0
while True:
    i += 1
    next = []
    while cur:
        R, B = cur.pop()
        Ry, Rx = R
        By, Bx = B
        if visit[Ry][Rx][By][Bx]:
            continue
        R_R = moveR(Ry, Rx)
        R_L = moveL(Ry, Rx)
        R_U = moveU(Ry, Rx)
        R_D = moveD(Ry, Rx)
        B_R = moveR(By, Bx)
        B_L = moveL(By, Bx)
        B_U = moveU(By, Bx)
        B_D = moveD(By, Bx)

        if B_R!=-1:
            if R_R==-1:
                end = True
                print(i)
                break
            else:
                if R_R==B_R:
                    if Rx<Bx:
                        R_R[1] -= 1
                    else:
                        B_R[1] -= 1
                next.append([R_R, B_R])
        if B_L!=-1:
            if R_L==-1:
                end = True
                print(i)
                break
            else:
                if R_L==B_L:
                    if Rx<Bx:
                        B_L[1] += 1
                    else:
                        R_L[1] += 1
                next.append([R_L, B_L])
        if B_U!=-1:
            if R_U==-1:
                end = True
                print(i)
                break
            else:
                if R_U==B_U:
                    if Ry<By:
                        B_U[0] += 1
                    else:
                        R_U[0] += 1
                next.append([R_U, B_U])
        if B_D!=-1:
            if R_D==-1:
                end = True
                print(i)
                break
            else:
                if R_D==B_D:
                    if Ry<By:
                        R_D[0] -= 1
                    else:
                        B_D[0] -= 1
                next.append([R_D, B_D])
        
        visit[Ry][Rx][By][Bx] = 1
    if not next:
        break
    cur += next
    if end==True:
        break
if not end:
    print(-1)
