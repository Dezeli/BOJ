# 좋다
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for i in range(N):
    find = nums[i]
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == find:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            else:
                cnt += 1
                break
        elif nums[l] + nums[r] > find:
            r -= 1
        elif nums[l] + nums[r] < find:
            l += 1

print(cnt)
