# 최소비용 구하기
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
M = int(input())

buses = defaultdict(list)

for _ in range(M):
    A, B, cost = map(int, input().split(" "))
    buses[A].append([B, cost])

start, end = map(int, input().split(" "))

def cal_cost(root, end):
    costs = [sys.maxsize for _ in range(N+1)]
    queue = deque([[root, 0]])

    while queue:
        s, stack_cost = queue.popleft()
        if stack_cost > costs[s]:
            continue
        for e, cost in buses[s]:
            if costs[e] > stack_cost + cost:
                costs[e] = stack_cost + cost
                queue.append([e, stack_cost + cost])
    return costs[end]

print(cal_cost(start, end))