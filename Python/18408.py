# 3 つの整数 (Three Integers)

nums = list(map(int, input().split()))

if sum(nums) >= 5:
    print(2)
else:
    print(1)
