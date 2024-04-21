# 내리막길
import sys
import heapq

input = sys.stdin.readline

M, N = map(int, input().split())

heap = []
road = []
dp = [[0]*N for _ in range(M)]
dp[0][0] = 1

for i in range(M):
    line = list(map(int, input().split()))
    road.append(line)
    for j in range(N):
        heapq.heappush(heap, [-line[j], i, j])

while heapq:
    h, i, j = heapq.heappop(heap)
    if i==M-1 and j==N-1:
        break
    cur = dp[i][j]
    if cur>0:
        if i>0 and road[i-1][j] < road[i][j]:
            dp[i-1][j] += cur
        if j>0 and road[i][j-1] < road[i][j]:
            dp[i][j-1] += cur
        if i<M-1 and road[i+1][j] < road[i][j]:
            dp[i+1][j] += cur
        if j<N-1 and road[i][j+1] < road[i][j]:
            dp[i][j+1] += cur
print(dp[M-1][N-1])
