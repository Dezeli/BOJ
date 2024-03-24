# 소가 길을 건너간 이유 5
import sys

input = sys.stdin.readline

N, K, B = map(int, input().split())

lights = [0 for _ in range(N+1)]
for _ in range(B):
    broken = int(input())
    lights[broken] = 1

cur = 0
for i in range(1, K+1):
    cur += lights[i]

min_fix = cur
for i in range(K+1, N+1):
    cur += lights[i]
    cur -= lights[i-K]
    min_fix = min(min_fix, cur)
print(min_fix)


