# 반도체 설계
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
conductor = list(map(int, input().split()))

cnt = [conductor[0]]
for i, port in enumerate(conductor):
    if cnt[-1] < port:
        cnt.append(port)
    else:
        search = bisect_left(cnt, port)
        cnt[search] = port

print(len(cnt))
