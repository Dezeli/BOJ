# Triangles

T = int(input())

for i in range(T):
    n, s = input().split()
    n = int(n)

    for j in range(1, n + 1):
        print(s * j)

        if s == "Z":
            s = "A"
        else:
            s = chr(ord(s) + 1)

    if i != T - 1:
        print()
