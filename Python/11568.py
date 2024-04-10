# 민균이의 계략
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