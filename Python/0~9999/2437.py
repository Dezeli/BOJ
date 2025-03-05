# 저울
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
weights.sort()

num = 1
for w in weights:
    if w > num:
        break
    num += w

print(num)