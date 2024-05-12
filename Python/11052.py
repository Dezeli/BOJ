# 카드 구매하기
import sys

input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))

costs = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, i + 1):
        costs[i] = max(costs[i], P[j] + costs[i - j])
print(costs[N])
