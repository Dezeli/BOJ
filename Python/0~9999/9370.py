# 미확인 도착지
import sys
from collections import deque
input = sys.stdin.readline

MAX_d = 10**7

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    roads = [[] for _ in range(n+1)]
    for __ in range(m):
        a, b, d = map(int, input().split())
        roads[a].append([b, d])
        roads[b].append([a, d])
    
    candidates = sorted([int(input()) for _ in range(t)])
    min_d = [MAX_d for _ in range(n+1)]
    smell = [False for _ in range(n+1)]

    move = deque([])
    move.append([0, s, False])
    while move:
        d, a, e = move.popleft()
        if min_d[a] >= d:

            if min_d[a] > d:
                smell[a] = e
            else:
                if e:
                    smell[a] = e
            min_d[a] = d
            
            for b, d1 in roads[a]:
                if (g==a and h==b) or (g==b and h==a) or e:
                    move.append([d+d1, b, True])
                else:
                    move.append([d+d1, b, False])

    ans = []
    for i in candidates:
        if smell[i]:
            ans.append(i)
    print(*ans)