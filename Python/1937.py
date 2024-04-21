# 욕심쟁이 판다
import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
forest = []
dp = [[1]*n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    forest.append(line)
    for j in range(n):
        heapq.heappush(heap, [line[j], i, j])

while heap:
    h, i, j = heapq.heappop(heap)
    cur = dp[i][j]
    if i>0 and forest[i-1][j] > forest[i][j]:
        dp[i-1][j] = max(cur+1, dp[i-1][j])
    if j>0 and forest[i][j-1] > forest[i][j]:
        dp[i][j-1] = max(cur+1, dp[i][j-1])
    if i<n-1 and forest[i+1][j] > forest[i][j]:
        dp[i+1][j] = max(cur+1, dp[i+1][j])
    if j<n-1 and forest[i][j+1] > forest[i][j]:
        dp[i][j+1] = max(cur+1, dp[i][j+1])

print(max([max(line) for line in dp]))