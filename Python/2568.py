# 전깃줄 - 2
import sys
from collections import deque
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    i, line = map(int, input().split())
    A.append([i, line])
A.sort()

cnt = [A[0][1]]
idx = [[]]
for i, n in A:
    if cnt[-1] < n:
        cnt.append(n)
        idx.append([i])
    else:
        search = bisect_left(cnt, n)
        cnt[search] = n
        idx[search].append(i)

print(N - len(cnt))

suyeol = deque([])
suyeol.appendleft(idx.pop().pop())
while idx:
    choose = idx.pop()
    i = choose.pop()
    while i >= suyeol[0]:
        i = choose.pop()
    suyeol.appendleft(i)

s = 0
suyeol.append(0)
for i, n in A:
    if i == suyeol[s]:
        s += 1
    else:
        print(i)
