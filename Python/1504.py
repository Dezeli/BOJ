# 특정한 최단 경로
import sys
<<<<<<< HEAD
import heapq
from collections import defaultdict
=======
from collections import defaultdict, deque
>>>>>>> 590f4c36037fa7889612d56804d8e0406bea85af

input = sys.stdin.readline
N, E = map(int, input().split(" "))
Graph = defaultdict(list)

for _ in range(E):
    u, v, d = map(int, input().split(" "))
    Graph[u].append([d, v])
    Graph[v].append([d, u])
v1, v2 = map(int, input().split(" "))
<<<<<<< HEAD
=======

>>>>>>> 590f4c36037fa7889612d56804d8e0406bea85af

def short_move(start, final):
    short_distance = [sys.maxsize for _ in range(N+1)]
    short_distance[start] = 0
<<<<<<< HEAD
    moves = [[0, start]]
    while moves:
        d, u = heapq.heappop(moves)
        if d > short_distance[u]: continue
        for w, v in Graph[u]:
            if short_distance[v] > short_distance[u] + w:
                short_distance[v] = short_distance[u] + w
                heapq.heappush(moves, [short_distance[v], v])
=======

    moves = deque(Graph[start])

    while moves:
        v, d = moves.popleft()
        if v==final:
            short_distance[final] = min([short_distance[final], d])
            continue
        else:
            if short_distance[v]<=d:
                continue
            else:
                short_distance[v] = d
                for newv, newd in Graph[start]:
                    moves.append([newv, newd+d])
>>>>>>> 590f4c36037fa7889612d56804d8e0406bea85af
    return short_distance[final]

route1 = short_move(1, v1)+ short_move(v1, v2) + short_move(v2, N)
route2 = short_move(1, v2)+ short_move(v2, v1) + short_move(v1, N)

<<<<<<< HEAD
if min([route1, route2]) < sys.maxsize:
    print(min([route1, route2]))
else:
    print(-1)
=======
route1 = short_move(1, v1)+ short_move(v1, v2) + short_move(v2, N)
route2 = short_move(1, v2)+ short_move(v2, v1) + short_move(v1, N)
print(min([route1, route2]))
>>>>>>> 590f4c36037fa7889612d56804d8e0406bea85af
