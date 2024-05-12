# 음악프로그램
import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

order = defaultdict(list)
check = [False for _ in range(N + 1)]
rec_check = [[False] * (N + 1) for _ in range(N + 1)]
right_order = []
rec = False

for _ in range(M):
    pd = list(map(int, input().split()))
    for i in range(1, len(pd) - 1):
        order[pd[i + 1]].append(pd[i])


def make_line(n):
    global rec
    for i in order[n]:
        if check[i]:
            continue
        if rec_check[n][i]:
            rec = True
            return
        rec_check[n][i] = True
        make_line(i)
        check[i] = True
    right_order.append(n)
    check[n] = True


for i in range(1, N + 1):
    if check[i]:
        continue
    make_line(i)

if rec:
    print(0)
else:
    for i in right_order:
        print(i)
