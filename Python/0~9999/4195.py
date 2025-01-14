# 친구 네트워크
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())


def find(P, a):
    if P[a]==a:
        return a
    else:
        return find(P, P[a])

def union(P, a, b):
    A = find(P, a)
    B = find(P, b)

    if A!=B:
        P[a] = min(A, B)
        P[b] = min(A, B)

for _ in range(T):
    parent = defaultdict(lambda x: x)
    child = defaultdict(int)
    F = int(input())
    P = min(input().rstrip().split())
    cnt = 2
    for i in range(F-1):
        a, b = input().rstrip().split()