# 세 용액
import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.sort()
min_Sum = sys.maxsize


for i in range(N - 2):
    start = i + 1
    end = N - 1
    while start < end:
        take = nums[i] + nums[start] + nums[end]
        if abs(take) < min_Sum:
            min_Sum = abs(take)
            result = [nums[i], nums[start], nums[end]]
        if take < 0:
            start += 1
        elif take > 0:
            end -= 1
        else:
            break

print(*result)
