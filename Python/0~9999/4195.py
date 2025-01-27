# 친구 네트워크
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())


def find(a):
    if P[a] != a:
        P[a] = find(P[a])
    return P[a]


def union(a, b):
    A = find(a)
    B = find(b)

    if A != B:
        P[B] = A
        C[A] += C[B]

    print(C[A])


class key_dict(dict):
    def __missing__(self, key):
        self[key] = key
        return self[key]


for _ in range(T):
    P = key_dict()
    C = defaultdict(lambda: 1)
    F = int(input())

    for i in range(F):
        a, b = input().rstrip().split()
        union(a, b)
