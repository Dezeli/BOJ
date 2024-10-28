# Andando no tempo

nums = list(map(int, input().split()))
nums.sort()

if nums[2] == nums[0] + nums[1]:
    print("S")
elif nums[0] == nums[1] or nums[1] == nums[2]:
    print("S")
else:
    print("N")
