# ACM Craft
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    process = [0 for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    queue = deque()

    for __ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        process[b] += 1

    W = int(input().rstrip())

    for i in range(1, N + 1):
        if process[i] == 0:
            queue.append(i)
            dp[i] = D[i - 1]

    while queue:
        bulid = queue.popleft()

        for i in graph[bulid]:
            process[i] -= 1
            dp[i] = max(dp[i], dp[bulid] + D[i - 1])
            if process[i] == 0:
                queue.append(i)

    print(dp[W])