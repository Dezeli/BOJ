# 바이러스
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

com_Graph = defaultdict(list)
virus = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    com_Graph[a].append(b)
    com_Graph[b].append(a)

def attack(num):
    if num in virus:
        return
    else:
        virus.append(num)
        for i in com_Graph[num]:
            attack(i)
attack(1)
print(len(virus)-1)