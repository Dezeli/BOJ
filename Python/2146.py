# 카드2

N = int(input())
nums = [i for i in range(1, N+1)]
while len(nums)!=1:
    if len(nums)%2==1:
        nums = [nums[-1]] + [nums[i] for i in range(1, len(nums), 2)]
    else:
        nums = [nums[i] for i in range(1, len(nums), 2)]

print(nums[0])