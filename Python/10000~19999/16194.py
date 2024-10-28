# 카드 구매하기 2
import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

dp = [0] + [i for i in cards]


for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] = min(dp[j] + dp[i - j], dp[i])

print(dp[N])
