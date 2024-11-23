# 얼마?

T = int(input())

for _ in range(T):
    cost = 0

    s = int(input())
    cost += s
    n = int(input())

    for __ in range(n):
        q, p = map(int, input().split())
        cost += q * p

    print(cost)
