# 두 용액
import sys

input = sys.stdin.readline

N = int(input())
liq = sorted(list(map(int, input().split())))


l = 0
r = N-1
ansl = l
ansr = r
min_comb = 2000000000 

while l < r:
    comb = liq[l] + liq[r]
    if comb==0:
        ansl = l
        ansr = r
        break

    if abs(comb) < min_comb:
        min_comb = abs(comb)
        ansl = l
        ansr = r
    if comb > 0:
        r -= 1
    else:
        l += 1
print(liq[ansl], liq[ansr])