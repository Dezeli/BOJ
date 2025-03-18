# 게임을 만든 동준이
import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
nums.reverse()

last = nums[0]

cnt = 0
for i in nums[1:]:
    if last <= i:
        cnt += 1 + i - last
        last -= 1
    else:
        last = i

print(cnt)
