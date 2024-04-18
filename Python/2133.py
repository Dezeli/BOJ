# 타일 채우기
import sys

input = sys.stdin.readline

N = int(input())

if N%2==1:
    print(0)
else:
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    for i in range(2, N+1):
        for j in range(0, i-2, 2):
            dp[i] += dp[j]*2
        dp[i] += dp[i-2]*3
    print(dp[N])