# 스네이크버드
import sys

input = sys.stdin.readline

N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in h:
    if L >= i:
        L += 1
print(L)
