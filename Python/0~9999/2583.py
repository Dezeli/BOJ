# 영역 구하기
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def cnt_land(x, y):
    global M, N, cnt
    if x<0 or y<0:
        return
    if x>=N or y>=M:
        return
    if visit[y][x] == 1:
        return
    visit[y][x] = 1
    cnt += 1
    
    cnt_land(x, y-1)
    cnt_land(x-1, y)
    cnt_land(x+1, y)
    cnt_land(x, y+1)


M, N, K = map(int, input().split())

visit = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            visit[j][i] = 1


total = 0
amt = []
for i in range(N):
    for j in range(M):
        if visit[j][i] == 1:
            continue
        cnt = 0
        cnt_land(i, j)
        total += 1
        amt.append(cnt)

amt.sort()

print(total)
print(*amt)