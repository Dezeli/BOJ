# 네 번째 점
from collections import defaultdict

xnums = defaultdict(int)
ynums = defaultdict(int)
for _ in range(3):
    x, y = map(int, input().split())
    xnums[x] += 1
    ynums[y] += 1

for n, i in xnums.items():
    if i == 1:
        print(n, end=" ")
for n, i in ynums.items():
    if i == 1:
        print(n)
