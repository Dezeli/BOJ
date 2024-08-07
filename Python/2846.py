# 오르막길
import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

max_up = 0
start = nums[0]
lasti = nums[0]

for i in nums:
    if i <= lasti:
        max_up = max(max_up, lasti - start)
        start = i
    lasti = i
max_up = max(max_up, lasti - start)

print(max_up)
