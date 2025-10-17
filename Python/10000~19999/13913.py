# 숨바꼭질 4
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

move = deque([])
move.append([N, N])

visit = [0 for _ in range(200001)]

while move:
    s, c = move.popleft()
    if s<0 or s>200000:
        continue
    if visit:
        continue
    visit[s] = c
    
    if s==K:
        break

    move.append([s+1, s])
    move.append([s-1, s])
    move.append([s*2, s])

print(visit[K])

reversed_route = []

last = K
while True:
    reversed_route.append(visit[last])
    if visit[last]==last:
        break
    last = visit[last]

print(len(reversed_route))
print(*reversed(reversed_route))
