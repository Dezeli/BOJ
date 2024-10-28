# 전자레인지
import sys

T = int(sys.stdin.readline().rstrip())
A = T // 300
T -= A * 300
B = T // 60
T -= B * 60
C = T // 10
T -= C * 10
if T != 0:
    print(-1)
else:
    print(A, B, C)
