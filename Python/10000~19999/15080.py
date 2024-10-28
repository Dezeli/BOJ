# Every Second Counts
import sys

H1, M1, S1 = map(int, sys.stdin.readline().split(" : "))
H2, M2, S2 = map(int, sys.stdin.readline().split(" : "))
result = 0
if S2 < S1:
    result += 60 + S2 - S1
    M2 -= 1
else:
    result += S2 - S1
if M2 < M1:
    result += 3600 + 60 * (M2 - M1)
    H2 -= 1
else:
    result += 60 * (M2 - M1)

if H2 < H1:
    H2 += 24
result += 3600 * (H2 - H1)
print(result)
