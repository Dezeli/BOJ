# 회사에 있는 사람
import sys
from collections import defaultdict

input = sys.stdin.readline

company = defaultdict(int)

n = int(input())

for _ in range(n):
    name, status = input().rstrip().split()
    if status=="enter":
        company[name] = 1
    else:
        company[name] = 0

names = []
for key, val in company.items():
    if val==1:
        names.append(key)
names.sort(reverse=True)

for name in names:
    print(name)