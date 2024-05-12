# 꼬인 전깃줄
import sys
from bisect import bisect_left

input = sys.stdin.readline

while True:
    try:
        n = int(input())
        stocks = list(map(int, input().split()))

        cnt = [stocks[0]]
        for s in stocks:
            if cnt[-1] < s:
                cnt.append(s)
            else:
                search = bisect_left(cnt, s)
                cnt[search] = s

        print(len(cnt))
    except:
        break
