# 주식
import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())

for case in range(1, T+1):
    N = int(input())
    chips = [int(input()) for _ in range(N)]

    ans = [chips[0]]

    for n in chips:
        if ans[-1] < n:
            ans.append(n)
        else:
            i = bisect_left(ans, n)
            ans[i] = n
    print(len(ans))

