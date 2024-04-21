# 가장 큰 정사각형
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [input() for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]=='0':
            continue
        if i==0 or j==0:
            dp[i][j] = 1
            continue
        
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(max([max(l) for l in dp])**2)