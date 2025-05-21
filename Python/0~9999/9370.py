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
        if (a==g and b==h) or (a==h and b==g):
            smell = d

    candidates = sorted([int(input()) for _ in range(t)])
    min_s = [MAX_d for _ in range(n+1)]
    min_g = [MAX_d for _ in range(n+1)]
    min_h = [MAX_d for _ in range(n+1)]
    move = deque([])
    move.append([0, s])
    while move:
        d, a = move.popleft()
        if min_s[a] > d:
            min_s[a] = d
            for b, d1 in roads[a]:
                move.append([d+d1, b])
    
    move.append([0, g])
    while move:
        d, a = move.popleft()
        if min_g[a] > d:
            min_g[a] = d
            for b, d1 in roads[a]:
                move.append([d+d1, b])
    
    move.append([0, h])
    while move:
        d, a = move.popleft()
        if min_h[a] > d:
            min_h[a] = d
            for b, d1 in roads[a]:
                move.append([d+d1, b])

    ans = []
    for i in candidates:
        visit = min(min_s[g] + min_h[i], min_s[h] + min_g[i]) + smell
        if visit==min_s[i]:
            ans.append(i)
    
    print(*ans)