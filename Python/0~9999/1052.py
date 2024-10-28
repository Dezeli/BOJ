# 물병
import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())

add = 0
waters = defaultdict(int)
waters[1] = N
water = sum(waters.values())

while water > K:
    new_waters = defaultdict(int)
    for key, val in waters.items():
        next, cur = divmod(val, 2)
        if next != 0:
            new_waters[key + 1] += next
        if cur == 1:
            new_waters[key] = cur
    if waters == new_waters:
        waters = new_waters
        waters[min(waters.keys())] += 1
        add += 2 ** (min(waters.keys()) - 1)
    else:
        waters = new_waters
    water = sum(waters.values())

print(add)
