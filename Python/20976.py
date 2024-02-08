# 2 番目に大きい整数 (The Second Largest Integer)

nums = list(map(int, input().split()))

nums.sort()
print(nums[1])