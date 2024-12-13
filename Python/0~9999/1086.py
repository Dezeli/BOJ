# 박성원
import sys
import itertools

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
K = int(input())
nums = [str(i) for i in nums]


case = list(itertools.permutations(nums, N))
cnt = 0

for i in case:
    if int(''.join(i))%K==0:
        cnt += 1
print(cnt)