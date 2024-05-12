# 점수 계산
import sys

input = sys.stdin.readline
scores = []
big_scores = []

for _ in range(8):
    n = int(input())
    scores.append(n)
    big_scores.append(n)

big_scores.sort(reverse=True)

print(sum(big_scores[:5]))

idx = []
for i in big_scores[:5]:
    idx.append(scores.index(i) + 1)
idx.sort()
print(*idx)
