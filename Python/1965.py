# 상자넣기
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))

ans = [box[0]]

for b in box:
    if ans[-1] < b:
        ans.append(b)
    else:
        i = bisect_left(ans, b)
        ans[i] = b

print(len(ans))
