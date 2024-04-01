# 카드
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
nums = defaultdict(int)

for _ in range(N):
    nums[int(input())] += 1


max_cnt = 0
max_num = []
for key, val in nums.items():
    if val==max_cnt:
        max_num.append(key)
    elif val>max_cnt:
        max_num = [key]
        max_cnt = val
max_num.sort()
print(max_num[0])