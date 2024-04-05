# 가장 긴 증가하는 부분 수열 2
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = [A[0]]

for n in A:
    if ans[-1] < n:
        ans.append(n)
    else:
        i = bisect_left(ans, n)
        ans[i] = n

print(len(ans))