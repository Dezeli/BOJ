# 숨바꼭질 3
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split(" "))

Location = [0 for _ in range(K * 2 + 1)]

if K <= N:
    print(N - K)
else:
    root = deque([[N, 1]])

    while root:
        pos, time = root.popleft()
        while True:
            if pos == 0:
                Location[pos] = time
                if not Location[pos + 1]:
                    root.append([pos + 1, time + 1])
                break
            if pos < K * 2:
                if not Location[pos]:
                    Location[pos] = time
                if not Location[pos + 1]:
                    root.append([pos + 1, time + 1])
                if not Location[pos - 1]:
                    root.append([pos - 1, time + 1])
                pos *= 2
            else:
                break
        if Location[K]:
            break
    print(Location[K] - 1)
