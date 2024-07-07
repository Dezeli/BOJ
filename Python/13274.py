# 수열
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

for _ in range(K):
    L, R, X = map(int, input().split())
    for i in range(L-1, R):
        nums[i] += X
    nums.sort()

print(*nums)