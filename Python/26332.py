# Buying in Bulk

n = int(input())

for _ in range(n):
    c, p = map(int, input().split())
    print(c, p)
    print(c * p - 2 * (c - 1))
