# 주식
import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    stock = list(map(int, input().split()))

    ans = [stock[0]]

    for n in stock:
        if ans[-1] < n:
            ans.append(n)
        else:
            i = bisect_left(ans, n)
            ans[i] = n

    print(f"Case #{case}")
    if len(ans) >= K:
        print(1)
    else:
        print(0)
