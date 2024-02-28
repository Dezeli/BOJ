# 팰린드롬?
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]

M = int(input())

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if nums[i]==nums[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for k in range(N-2):
    for i in range(N-2-k):
        j = i+2+k
        if nums[i]==nums[j] and dp[i+1][j-1]==1:
            dp[i][j] = 1

for i in range(M):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])