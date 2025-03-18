# 팔
import sys

input = sys.stdin.readline

L, R = map(int, input().split())

ans = 0
if len(str(L)) == len(str(R)):
    l, r = str(L), str(R)
    for l1, r1 in zip(l, r):
        if l1 == r1:
            if l1 == "8":
                ans += 1
        else:
            break
print(ans)
