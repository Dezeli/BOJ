# 카드 게임
import sys
from bisect import bisect_right

input = sys.stdin.readline

N, M, K = map(int, input().split())
cards = sorted(list(map(int, input().split())))
use = [0 for _ in range(M)]

for i in map(int, input().split()):
    for j in range(bisect_right(cards, i), M):
        if use[j]:
            continue
        use[j] = 1
        print(cards[j])
        break
