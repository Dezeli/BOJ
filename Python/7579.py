# 앱
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

max_cost = sum(costs)+1

max_byte = [0 for _ in range(max_cost)]

for i in range(N):
    m, c= memories[i], costs[i]
    for j in range(max_cost-1, c-1, -1):
        max_byte[j] = max(max_byte[j], m + max_byte[j-c])


for i in range(max_cost):
    if max_byte[i]>=M:
        print(i)
        break
