# 수열
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))


sum_num = sum([nums[i] for i in range(K)])
l = 0
r = K - 1

max_sum = -(10**8)

while True:
    max_sum = max(max_sum, sum_num)

    sum_num -= nums[l]
    l += 1
    r += 1
    if r == N:
        break
    sum_num += nums[r]

print(max_sum)
