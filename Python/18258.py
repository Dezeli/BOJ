# 큐 2
import sys
from collections import deque

input = sys.stdin.readline

queue = deque([])

N = int(input())

for _ in range(N):
    order = input().rstrip()

    if order == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        order, n = order.split()
        queue.append(n)
