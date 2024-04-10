# 전구
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
idx = [[]]
for i, n in enumerate(A):
    match = B_pos[n]
    if cnt[-1] < match:
        cnt.append(match)
        idx.append([i])
    else:
        search = bisect_left(cnt, match)
        cnt[search] = match
        idx[search].append(i)

print(len(cnt))

suyeol = deque([])
suyeol.appendleft(idx.pop().pop())
while idx:
    choose = idx.pop()
    i = choose.pop()
    while i >= suyeol[0]:
        i = choose.pop()
    suyeol.appendleft(i)

print(*sorted([A[i] for i in suyeol]))