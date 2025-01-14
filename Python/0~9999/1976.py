# 여행가자
import sys

input = sys.stdin.readline

def find(P, x):
    if P[x] != x:
        P[x] = find(P, P[x])
    return P[x]

def union(P, a, b):
    A = find(P, a)
    B = find(P, b)
    if A != B:
        P[B] = A

N = int(input())
M = int(input())

P = [i for i in range(N+1)]

for i in range(1, N+1):
    roads = list(map(int, input().split()))
    for j in range(1, N+1):
        if roads[j-1] == 1:
            union(P, i, j)

trip = list(map(int, input().split()))

root = find(P, trip[0])
pos = True
for city in trip:
    if find(P, city) != root:
        pos = False
        break

print("YES" if pos else "NO")