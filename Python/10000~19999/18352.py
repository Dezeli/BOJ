# 특정 거리의 도시 찾기
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

road = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    road[A].append(B)

visit = [N+1]*(N+1)

move = deque([[0, X]])

result = []
while move:
    d, c = move.popleft()
    if visit[c] <= d:
        continue
    visit[c] = d
    if d==K:
        result.append(c)
    
    for c1 in road[c]:
        move.append([d+1, c1])


if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)