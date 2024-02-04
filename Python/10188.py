# Quadrilateral

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    for __ in range(y):
        print("X"*x)
    print()