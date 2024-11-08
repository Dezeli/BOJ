# 공항
import sys
from bisect import bisect_right

input = sys.stdin.readline

G = int(input())
P = int(input())

gate = [i for i in range(G + 1)]

cnt = 0
able = True
for _ in range(P):
    g = int(input())
    if not able:
        continue
    best = bisect_right(gate, g) - 1
    if gate[best] == 0:
        able = False
    else:
        cnt += 1
        gate.pop(best)

print(cnt)
