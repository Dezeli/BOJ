# 방학 숙제
import sys

L = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

math = A // C + 1
kor = B // D + 1
if A % C == 0:
    math -= 1
if B % D == 0:
    kor -= 1

print(min([L - math, L - kor]))
