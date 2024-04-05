# 가장 긴 증가하는 부분 수열 4
import sys
from collections import deque
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cnt = [A[0]]
idx = [[]]
for i, n in enumerate(A):
    if cnt[-1] < n:
        cnt.append(n)
        idx.append([i])
    else:
        search = bisect_left(cnt, n)
        cnt[search] = n
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

print(*[A[i] for i in suyeol])