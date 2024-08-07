# 풍선 놀이
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

slot = [1 for _ in range(N + 1)]
slot[0] = 0

for _ in range(Q):
    L, I = map(int, input().split())
    for i in range(L, N + 1, I):
        slot[i] = 0

print(sum(slot))
