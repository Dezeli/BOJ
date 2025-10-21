# Strongly Connected Component
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V,  E = map(int, input().split())

graph = defaultdict(list)

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)



index = 0
numbers = [-1] * (V + 1)
lowlink = [0] * (V + 1)
on_stack = [False] * (V + 1)
stack = []
SCCs = []

def tarjan(v):
    global index
    numbers[v] = lowlink[v] = index
    index += 1
    stack.append(v)
    on_stack[v] = True

    for w in graph[v]:
        if numbers[w] == -1:
            tarjan(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif on_stack[w]:
            lowlink[v] = min(lowlink[v], numbers[w])

    if lowlink[v] == numbers[v]:
        scc = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            scc.append(w)
            if w == v:
                break
        SCCs.append(sorted(scc))

for v in range(1, V + 1):
    if numbers[v] == -1:
        tarjan(v)

SCCs.sort(key=lambda x: x[0])

print(len(SCCs))
for scc in SCCs:
    print(*scc, -1)