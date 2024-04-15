# 01타일
import sys

input = sys.stdin.readline

N = int(input())

nums = [0 for _ in range(N+1)]
nums[0] = 1
nums[1] = 2

for i in range(2, N):
    nums[i] = (nums[i-2] + nums[i-1])%15746

print(nums[N-1])