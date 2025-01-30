# 캠핑
import sys

input = sys.stdin.readline

i = 0
while True:
    i += 1
    L, P, V = map(int, input().split())

    if L == P == V == 0:
        break

    use = 0

    while V - P >= 0:
        use += L
        V -= P
    use += min(V, L)

    print(f"Case {i}: {use}")
