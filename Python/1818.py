# 책정리
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
books = list(map(int, input().split()))

ans = [books[0]]

for n in books:
    if ans[-1] < n:
        ans.append(n)
    else:
        i = bisect_left(ans, n)
        ans[i] = n

print(N-len(ans))