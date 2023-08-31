# Cow Multiplication
import sys

N1, N2 = map(str, sys.stdin.readline().split())
result = 0
N2 = [int(i) for i in N2]
N2 = sum(N2)
for i in N1:
    result += int(i) * N2
print(result)
