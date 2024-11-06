# 벽 부수고 이동하기 4
import sys

input = sys.stdin.readline

N, M = map(int, input().split())


board = [input().rstrip() for _ in range(N)]

group = [[0]*M for _ in range(N)]
cnt = [0 for _ in range(N*M+1)]

g = 0
c = 0
for i in range(N):
    for j in range(M):
        if board[i][j]=='1':
            continue
        if group[i][j]!=0:
            continue
        g += 1
        group[i][j] = g
        c += 1
        move = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        while move:
            a, b = move.pop()
            if not (0<=a<N):
                continue
            if not (0<=b<M):
                continue
            if board[a][b]=='1':
                continue
            if group[a][b]!=0:
                continue
            c += 1
            group[a][b] = g
            move += [[a-1, b], [a+1, b], [a, b-1], [a, b+1]]
        cnt[g] = c
        c = 0


for i in range(N):
    l = ''
    for j in range(M):
        if board[i][j]=='0':
            l += '0'
            continue
        
        t = set()
        
        move = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        for a, b in move:
            if not (0<=a<N):
                continue
            if not (0<=b<M):
                continue
            t.add(group[a][b])
        
        sum_cnt = 1
        for k in t:
            sum_cnt += cnt[k]

        sum_cnt = sum_cnt%10
        l += str(sum_cnt)
    print(l)