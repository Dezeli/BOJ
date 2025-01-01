# 팰린드롬 개수 구하기 (Large)
import sys

input = sys.stdin.readline

MOD = 10007

S = ' ' + input().rstrip()
N = len(S) - 1

dp = [0]*(N+1)
prefix_sum_dp = [0]*(N+1)
for l in range(1, N+1):
    for r in range(l, N+1):
        if S[l] == S[r]:
            dp[r] += (prefix_sum_dp[N] - prefix_sum_dp[r] + 1) % MOD
        prefix_sum_dp[r] = (prefix_sum_dp[r - 1] + dp[r]) % MOD

print(prefix_sum_dp[N])