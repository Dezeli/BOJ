# 경로 찾기
from sys import stdin
from collections import defaultdict

N = int(stdin.readline().rstrip())
G = defaultdict(list)

for i in range(N):
    line = list(map(int, stdin.readline().split(" ")))
    for j in range(len(line)):
        if line[j] == 1:
            G[i].append(j)


for i in range(N):
    visit = [0 for _ in range(N)]
    queue = [] + G[i]
    while queue:
        n = queue.pop()
        if visit[n] == 0:
            visit[n] = 1
            queue += G[n]
    print(" ".join(str(i) for i in visit))
