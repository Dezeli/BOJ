# 근무 지옥에 빠진 푸앙이 (Large)
from collections import defaultdict
import sys

input = sys.stdin.readline

working_hours = defaultdict(int)
hours = {0: 4, 1: 6, 2: 4, 3: 10}

N = int(input().strip())
for i in range(N):
    for j in range(4):
        names = input().rstrip().split()
        for name in names:
            if name != "-":
                working_hours[name] += hours[j]

if not working_hours:
    min_num = 0
else:
    min_num = min(working_hours.values())

max_num = max(working_hours.values(), default=0)

if max_num - min_num > 12:
    print("No")
else:
    print("Yes")
