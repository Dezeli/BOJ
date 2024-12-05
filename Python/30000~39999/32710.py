# 구구단표

nums = set()

for i in range(2, 10):
    for j in range(1, 10):
        nums.add(i)
        nums.add(j)
        nums.add(i * j)

N = int(input())
if N in nums:
    print(1)
else:
    print(0)
