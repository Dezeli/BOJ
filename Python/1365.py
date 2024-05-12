# 꼬인 전깃줄
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
pole = list(map(int, input().split()))

cnt = [pole[0]]
for i, line in enumerate(pole):
    if cnt[-1] < line:
        cnt.append(line)
    else:
        search = bisect_left(cnt, line)
        cnt[search] = line

print(n - len(cnt))
