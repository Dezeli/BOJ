# LCS 4
import sys
from collections import deque
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B_pos = [0 for _ in range(N+1)]
for i, n in enumerate(B):
    B_pos[n] = i+1

cnt = [B_pos[A[0]]]
for i, n in enumerate(A):
    match = B_pos[n]
    if cnt[-1] < match:
        cnt.append(match)
    else:
        search = bisect_left(cnt, match)
        cnt[search] = match

print(len(cnt))