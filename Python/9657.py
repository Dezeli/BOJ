# 돌 게임 3
import sys

input = sys.stdin.readline

N = int(input())

dp = ['S' for _ in range(1001)]
dp[2] = 'C'

for i in range(6, N+1):
    if dp[i-1]=='S' and dp[i-3]=='S' and dp[i-4]=='S':
        dp[i] = 'C'

if dp[N]=='C':
    print("CY")
else:
    print("SK")