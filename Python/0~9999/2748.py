# 피보나치 수 2

n = int(input())
nums = [0 for _ in range(n + 1)]
nums[1] = 1

for i in range(2, n + 1):
    nums[i] = nums[i - 1] + nums[i - 2]
print(nums[n])
