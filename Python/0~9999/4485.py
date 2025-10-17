# 녹색 옷 입은 애가 젤다지?
import sys
import heapq

input = sys.stdin.readline

MAX_INT = 125*125*9

pro_num = 0
while True:
    N = int(input())
    if N==0:
        break
    pro_num += 1

    d2 = [list(map(int, input().split())) for _ in range(N)]
    visit = [[MAX_INT]*N for _ in range(N)]

    move = []
    heapq.heappush(move, [0, 0, 0])
    while move:
        m, x, y = heapq.heappop(move)
        if x<0 or y<0 or x>=N or y>=N:
            continue
        
        if visit[x][y] > m+d2[x][y]:
            visit[x][y] = m+d2[x][y]
            heapq.heappush(move, [m+d2[x][y], x+1, y])
            heapq.heappush(move, [m+d2[x][y], x-1, y])
            heapq.heappush(move, [m+d2[x][y], x, y+1])
            heapq.heappush(move, [m+d2[x][y], x, y-1])
    print(f"Problem {pro_num}: {visit[N-1][N-1]}")
