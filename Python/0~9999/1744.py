# 수 묶기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()
nums = deque(nums)

max_sum = 0

while len(nums) >= 2:
    a = nums.pop()
    b = nums.pop()

    if a > 0 and b > 0:
        if b == 1:
            max_sum += a + b
        else:
            max_sum += a * b
    elif a > 0:
        max_sum += a
        nums.append(b)
        break
    else:
        nums.append(b)
        nums.append(a)
        break

while len(nums) >= 2:
    a = nums.popleft()
    b = nums.popleft()
    max_sum += a * b

if nums:
    max_sum += nums.pop()

print(max_sum)
