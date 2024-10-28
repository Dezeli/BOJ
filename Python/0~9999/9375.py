# 패션왕 신해빈
import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())


for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    clothes = defaultdict(list)
    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split(" ")
        clothes[type].append(name)
    day = 1
    for val in clothes.values():
        day *= len(val) + 1
    print(day - 1)
