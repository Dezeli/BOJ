# 약물 복용
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
As, Ae, Bs, Be, Cs, Ce = map(int, input().split())

day = 1440

cur = Ae
suc = True
for i in range(1, N + 1):
    cur += K
    if cur < Bs:
        print("NO")
        suc = False
        break
    elif cur > Be:
        cur = Be
    cur += K
    if cur < Cs:
        print("NO")
        suc = False
        break
    elif cur > Ce:
        cur = Ce
    cur += K - day
    if cur < As:
        if i == N:
            continue
        print("NO")
        suc = False
        break
    elif cur > Ae:
        cur = Ae
if suc:
    print("YES")
