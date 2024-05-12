# 완전제곱수

M = int(input())
N = int(input())

nums = []

for i in range(M, N + 1):
    if i ** (1 / 2) == int(i ** (1 / 2)):
        nums.append(i)

if nums:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)
