# 부분수열의 합
import sys
from collections import Counter

input = sys.stdin.readline

N, S = map(int, input().split())
d1 = list(map(int, input().split()))


mid = N // 2
A, B = d1[:mid], d1[mid:]

def sums(nums):
    n = len(nums)
    sums = []
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if mask & (1 << i):
                s += nums[i]
        sums.append(s)
    return sums

left = sums(A)
right = sums(B)
right_cnt = Counter(right)

ans = 0
for v in left:
    ans += right_cnt[S - v]


if S == 0:
    ans -= 1
    
print(ans)