# 구간 합 구하기 4
import sys

N, M = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
nums_sum = [0]

for i in nums:
    nums_sum.append(nums_sum[-1]+i)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split(" "))
    print(nums_sum[j] - nums_sum[i-1])