# 피보나치 수
import sys

input = sys.stdin.readline
n = int(input())
p = (10**6)//10*15

dp = [0 for _ in range(p+1)]
dp[1] = 1

for i in range(2, p+1):
    dp[i] = (dp[i-1] + dp[i-2])%(10**6)

print(dp[n%p])
