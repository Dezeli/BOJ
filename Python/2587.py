# 대표값2
import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(5)]
nums.sort()
print(sum(nums)//5)
print(nums[2])