# 2408 (Easy)
import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

max_num = 0

def move(cnt, b):
    global max_num
    if cnt==0:
        for l in b:
            max_num = max(max_num, max(l))
        return
    
    b1, b2, b3, b4 = [], [], [], [] # 상 하 좌 우
    for i in range(N):
        l1, l2, l3, l4 = 0, 0, 0, 0
        r1, r2, r3, r4 = [], [], [], []   
        for j in range(N):
            # 상
            n1 = b[j][i]
            if n1!=0:
                if l1==0:
                    l1 = n1
                else:
                    if n1==l1:
                        r1.append(n1*2)
                        l1 = 0
                    else:
                        r1.append(l1)
                        l1 = n1
            # 하
            n2 = b[N-j-1][i]
            if n2!=0:
                if l2==0:
                    l2 = n2
                else:
                    if n2==l2:
                        r2.append(n2*2)
                        l2 = 0
                    else:
                        r2.append(l2)
                        l2 = n2
            # 좌
            n3 = b[i][j]
            if n3!=0:
                if l3==0:
                    l3 = n3
                else:
                    if n3==l3:
                        r3.append(n3*2)
                        l3 = 0
                    else:
                        r3.append(l3)
                        l3 = n3
            # 우
            n4 = b[i][N-j-1]
            if n4!=0:
                if l4==0:
                    l4 = n4
                else:
                    if n4==l4:
                        r4.append(n4*2)
                        l4 = 0
                    else:
                        r4.append(l4)
                        l4 = n4
        if l1:
            r1.append(l1)
        if l2:
            r2.append(l2)
        if l3:
            r3.append(l3)
        if l4:
            r4.append(l4)
        while len(r1)!=N:
            r1.append(0)
        while len(r2)!=N:
            r2.append(0)
        while len(r3)!=N:
            r3.append(0)
        while len(r4)!=N:
            r4.append(0)
        b1.append(r1)
        b2.append(r2)
        b3.append(r3)
        b4.append(r4)
    move(cnt-1, b1)
    move(cnt-1, b2)
    move(cnt-1, b3)
    move(cnt-1, b4)

move(5, board)
print(max_num)
        