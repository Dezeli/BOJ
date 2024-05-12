# 열차정렬
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]


def add(li, a):
    c = bisect_left(li, a)
    if c:
        if len(li) != c:
            li[c] = a
        else:
            li.append(a)


min_len = 0
for i in range(N):
    l, r = [A[i]], [-A[i]]
    for j in range(i + 1, N):
        add(l, A[j])
        add(r, -A[j])
    min_len = max(min_len, len(l) + len(r) - 1)
print(min_len)
