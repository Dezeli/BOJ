# 촌수 계산
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visit = [0] * (n + 1)

move = deque([[0, a]])

connect = False
while move:
    c, i = move.pop()

    if i == b:
        connect = True
        break
    if visit[i] == 1:
        continue
    visit[i] = 1

    for j in graph[i]:
        move.appendleft([c + 1, j])

if connect:
    print(c)
else:
    print(-1)
