# 징검다리
import sys
import math

input = sys.stdin.readline

T = int(input())
c = -2*int(1e16)
mx = int((-1 + math.sqrt(1-4*c))//2)+1

for _ in range(T):
    n = int(input())
    s, e, ans = 0, mx, 0
    while s < e:
        mid = (s+e)//2
        if (mid+1)*mid//2 <= n:
            ans = mid
            s = mid+1
        else:
            e = mid
    print(ans)