# ABCDE
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

friends = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

