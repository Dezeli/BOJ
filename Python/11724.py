# 연결 요소의 개수
import sys
import collections

N, M = map(int, sys.stdin.readline().split(" "))
graph = collections.defaultdict(list)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split(" "))
    graph[u].append(v)
    graph[v].append(u)
    
dots = [1]+ [0 for _ in range(N)]

sys.setrecursionlimit(10**9)
def linked(d):
    if dots[d]==1:
        return
    else:
        dots[d] = 1
        for i in graph[d]:
            linked(i)
        return

cnt  = 0
for i in range(1, N+1):
    if dots[i]:
        continue
    else:
        cnt += 1
        linked(i)
print(cnt)