# Breed Counting
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())


farm = [[0, 0, 0]]

for _ in range(N):
    id = int(input())
    if id==1:
        e = [1, 0, 0]
    elif id==2:
        e = [0, 1, 0]
    else:
        e = [0, 0, 1]
    
    cow = [farm[-1][i]+e[i] for i in range(3)]
    farm.append(cow)

for _ in range(Q):
    a, b = map(int, input().split())

    e = farm[b]
    s = farm[a-1]

    print(*[e[i]-s[i] for i in range(3)])