# 숨바꼭질 4
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    move = deque()
    move.append(x)
    while move: 
        x = move.popleft()
        if x==y:
            break
        for i in [x-1, x+1, x*2]:
            if 0<=i<100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                visited_route[i] = x
                move.append(i)


N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
visited_route = [0 for _ in range(100001)]
visited[N] = 1

bfs(N, K)

print(visited[K] - 1)

route = []
last = K
while last != N:
    route.append(last)
    last = visited_route[last]
route.append(N)

print(*route[::-1])