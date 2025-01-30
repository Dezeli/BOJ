# 트리
import sys

input = sys.stdin.readline

case = 0


def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]


def update(x, a):
    if P[x] == x:
        P[x] = a
        return
    update(P[x], a)
    P[x] = a


def union(a, b):
    A = find(a)
    B = find(b)

    if A < B:
        update(b, A)
    elif A > B:
        update(a, B)
    else:
        P[A] = 0


while True:
    case += 1
    n, m = map(int, input().split())
    if n == m == 0:
        break

    P = [i for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    tree = 0
    for i in range(1, n + 1):
        if P[i] == i:
            tree += 1

    if tree == 0:
        print(f"Case {case}: No trees.")
    elif tree == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree} trees.")
