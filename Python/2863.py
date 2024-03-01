# 이게 분수?

A, B = map(int, input().split())
C, D = map(int, input().split())

rotate = []

rotate.append(A/C+B/D)
rotate.append(C/D+A/B)
rotate.append(D/B+C/A)
rotate.append(B/A+D/C)

print(rotate.index(max(rotate)))
