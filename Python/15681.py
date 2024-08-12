# 트리와 쿼리
import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

trunks = defaultdict(list)
dir_trunks = defaultdict(list)
for _ in range(N-1):
    U, V = map(int, input().split())
    trunks[U].append(V)
    trunks[V].append(U)


queue = [R]
visit = [0 for _ in range(N+1)]

while queue:
    d = queue.pop()
    if visit[d]==1:
        continue

    visit[d] = 1
    for i in trunks[d]:
        if visit[i]==0:
            queue.append(i)
            dir_trunks[d].append(i)

sub = [0 for _ in range(N+1)]
def find_sub(n):
    for i in dir_trunks[n]:
        sub[n] += find_sub(i)
    sub[n] += 1
    
    return sub[n]

find_sub(R)

for _ in range(Q):
    U = int(input())
    print(sub[U])