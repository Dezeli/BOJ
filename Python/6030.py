# Scavenger Hunt

def get_divisor(n):
    data = set()
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            data.add(i)
            data.add(n // i)
    return sorted(data)

P, Q = map(int, input().split())
for i in get_divisor(P):
    for j in get_divisor(Q):
        print(i, j)