# 네 번째 수

nums = list(map(int, input().split()))

nums.sort()

if nums[1] - nums[0] == nums[2] - nums[1]:
    print(nums[2] * 2 - nums[1])
elif nums[1] - nums[0] < nums[2] - nums[1]:
    print(nums[2] - nums[1] + nums[0])
else:
    print(nums[1] * 2 - nums[2])
