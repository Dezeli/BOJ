# 和の判定 (Sum Checker)

A = int(input())
B = int(input())
C = int(input())

if sum([A, B, C]) == max([A, B, C]) * 2:
    print(1)
else:
    print(0)
