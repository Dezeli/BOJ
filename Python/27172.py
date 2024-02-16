# 수 나누기 게임
import sys

input = sys.stdin.readline

N = int(input())


cards = list(map(int, input().split()))
S = set(cards)
big = max(cards)
score = [0 for _ in range(big+1)]

for i in cards:
    for j in range(2*i, big+1, i):
        if j in S:
            score[i] += 1
            score[j] -= 1

print(*[score[i] for i in cards])