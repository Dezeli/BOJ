# 줄세우기
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

children = [int(input()) for _ in range(N)]
dp = [children[0]]

for c in children:
    if dp[-1] < c:
        dp.append(c)
    else:
        s = bisect_left(dp, c)
        dp[s] = c

print(N-len(dp))