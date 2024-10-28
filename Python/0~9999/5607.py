# 問題 １

n = int(input())

A, B = 0, 0

for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        A += a + b
    elif a == b:
        A += a
        B += b
    else:
        B += a + b

print(A, B)
