# 병사 배치하기
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
soldiers = list(map(int, input().split()))

cnt = [soldiers[0]]
for i, p in enumerate(soldiers):
    if cnt[-1] < -p:
        cnt.append(-p)
    else:
        search = bisect_left(cnt, -p)
        cnt[search] = -p

print(N - len(cnt))
