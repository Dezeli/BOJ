# 수 정렬하기 3
import sys

N = int(sys.stdin.readline().rstrip())
nums = [0 for i in range(10000)]
for _ in range(N):
    nums[int(sys.stdin.readline().rstrip()) - 1] += 1
i = 0
for j in nums:
    i += 1
    for _ in range(j):
        print(i)
