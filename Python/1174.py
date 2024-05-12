# 줄어드는 수
from itertools import combinations

N = int(input())
nums = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
down_nums = []

for i in range(1, 11):
    down_nums += [
        int("".join(sorted(i, reverse=True))) for i in list(combinations(nums, i))
    ]
down_nums.sort()


if N > len(down_nums):
    print(-1)
else:
    print(down_nums[N - 1])
