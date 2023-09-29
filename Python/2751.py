# 수 정렬하기 2
import sys

T = int(sys.stdin.readline())
nums = []
for i in range(T):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
    print(i)
