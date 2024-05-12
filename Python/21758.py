# 꿀 따기
import sys

input = sys.stdin.readline

N = int(input())
honeys = list(map(int, input().split()))
sum_honey = honeys[:]
max_sum = 0

for i in range(1, N):
    sum_honey[i] += sum_honey[i - 1]

for i in range(1, N - 1):
    max_sum = max(max_sum, 2 * sum_honey[-1] - honeys[0] - honeys[i] - sum_honey[i])

for i in range(1, N - 1):
    max_sum = max(max_sum, sum_honey[-1] - honeys[-1] - honeys[i] + sum_honey[i - 1])

for i in range(1, N - 1):
    max_sum = max(
        max_sum,
        sum_honey[i] - honeys[0] + sum_honey[-1] - sum_honey[i - 1] - honeys[-1],
    )

print(max_sum)
