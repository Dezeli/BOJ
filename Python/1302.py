# 베스트셀러
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
best = defaultdict(int)

for _ in range(N):
    book = input()
    best[book] += 1


max_cnt = 0
max_book = []
for key, val in best.items():
    if val == max_cnt:
        max_book.append(key)
    elif val > max_cnt:
        max_book = [key]
        max_cnt = val
max_book.sort()
print(max_book[0])
