# 게임 개발
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

time = [0]
build = [[]]

dp = [10**8 for _ in range(N+1)]
dp[0] = 0

for _ in range(N):
    data = list(map(int, input().split()))
    time.append(data[0])
    build.append(data[1:-1]+[0])

not_build = deque([i for i in range(1, N+1)])
while not_build:
    b = not_build.popleft()
    can = True
    max_t = 0
    for i in build[b]:
        if dp[i]==10**8:
            can = False
            break
        max_t = max(dp[i], max_t)
    
    if can:
        dp[b] = max_t + time[b]
    else:
        not_build.append(b)

for i in dp[1:]:
    print(i)