# 소형기관차
import sys

input = sys.stdin.readline
N = int(input())
trains = list(map(int, input().split()))
carry = int(input())

sum_train = [0]
for train in trains:
    sum_train.append(sum_train[-1] + train)

dp = [[0] * (N + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * carry, N + 1):
        if i == 1:
            dp[i][j] = max(dp[i][j - 1], sum_train[j] - sum_train[j - carry])
        else:
            dp[i][j] = max(
                dp[i][j - 1], dp[i - 1][j - carry] + sum_train[j] - sum_train[j - carry]
            )

print(dp[3][N])
