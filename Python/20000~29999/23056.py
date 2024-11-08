# 참가자 명단
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

squad = defaultdict(list)

while True:
    c, n = input().rstrip().split()
    if c == n == "0":
        break

    c = int(c)
    if len(squad[c]) < M:
        squad[c].append(n)

for i in range(1, N + 1, 2):
    students = squad[i]
    students.sort(key=lambda x: (len(x), x))
    for s in students:
        print(i, s)

for i in range(2, N + 1, 2):
    students = squad[i]
    students.sort(key=lambda x: (len(x), x))
    for s in students:
        print(i, s)
