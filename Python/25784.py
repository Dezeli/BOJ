# Easy-to-Solve Expressions

nums = list(map(int, input().split()))
nums.sort()

if nums[2]==nums[0]+nums[1]:
    print(1)
elif nums[2]==nums[0]*nums[1]:
    print(2)
else:
    print(3)