# 감소하는 수
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = "".join(list(map(str, reversed(list(j)))))
        result.append(int(num))

result.sort()
if N >= len(result):
    print(-1)
else:
    print(result[N])
