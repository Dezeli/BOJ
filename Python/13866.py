# Assigning Teams 
import sys

nums = list(map(int, sys.stdin.readline().split()))
team = max(nums) + min(nums)
nums.remove(max(nums))
nums.remove(min(nums))
print(abs(team - (sum(nums))))
