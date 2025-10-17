# ABCDE
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

friends = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

relation = []

def backtrack():
    if len(relation)==5:
        return True
    
    if relation:
        connection = friends[relation[-1]]   
    else:
        connection = [i for i in range(N)]
    for i in connection:
        if i in relation:
            continue
        relation.append(i)
        result = backtrack()
        relation.pop()
        if result:
            return True
    return False

result = backtrack()
if result:
    print(1)
else:
    print(0)