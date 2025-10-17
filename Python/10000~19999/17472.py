# 다리 만들기 2
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

d2 = [list(map(int, input().split())) for _ in range(N)]

visit = [[0]*M for _ in range(N)]

island = 0
for i in range(N):
    for j in range(M):
        if visit[i][j]:
            continue
        if d2[i][j]==0:
            continue
        island += 1
        move = [[i, j]]
        while move:
            x, y = move.pop()
            if x<0 or y<0 or x>=N or y>=M:
                continue
            if visit[x][y]:
                continue
            if d2[x][y]==0:
                continue
            visit[x][y] = 1
            d2[x][y] = island
            move.append([x+1, y])
            move.append([x-1, y])
            move.append([x, y+1])
            move.append([x, y-1])

dx = [1, 0]
dy = [0, 1]

def make_road(i, j):
    s = d2[i][j]
    for k in range(2):
        a = i
        b = j
        length = 0
        while True:
            a += dx[k]
            b += dy[k]
            if a<0 or b<0 or a>=N or b>=M:
                break
            if d2[a][b]!=0:
                if d2[a][b]!=s:
                    e = d2[a][b]
                    if length>=2:
                        heapq.heappush([length, s, e])
                break
            length += 1


roads = []
for i in range(N):
    for j in range(M):
        if d2[i][j]!=0:
            make_road(i, j)


connect = [0 for i in range()]
for d1 in d2:
    print(d1)
print(roads)