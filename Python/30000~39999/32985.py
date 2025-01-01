# 트리 부수기
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

tree = defaultdict(list)
result = [0 for _ in range(N)]
visit = [0 for _ in range(N)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

move = deque([])
for i in tree[0]:
    move.append([1, i])
visit[0] = 1

while move:
    c, n = move.popleft()
    if visit[n]==1:
        continue
    visit[n] = 1
    result[n] = (N-1+c)%2

    for i in tree[n]:
        move.append([c+1, i])

result = result[::-1]
result.pop()
for i in result:
    print(i, end="")
