# 동전
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0 for _ in range(10001)]
    dp[0] = 1
        
    for c in coin:
        for i in range(1, M+1):
            if i >= c:
                dp[i] += dp[i-c]
    print(dp[M])