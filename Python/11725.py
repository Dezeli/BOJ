# 트리의 부모 찾기
import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline().rstrip())

G = defaultdict(list)
P_Node = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    N1, N2 = map(int, sys.stdin.readline().split(" "))
    G[N1].append(N2)
    G[N2].append(N1)

root = [1]
check = deque(root)

while check:
    P = check.popleft()
    for i in G[P]:
        if P_Node[i]:
            continue
        P_Node[i] = P
        check.append(i)

for i in P_Node[2:]:
    print(i)
