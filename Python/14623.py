# 감정이입
import sys

A1 = "0b" + str(sys.stdin.readline().rstrip())
B1 = "0b" + str(sys.stdin.readline().rstrip())
A2 = int(A1, 2)
B2 = int(B1, 2)
print(format(A2 * B2, "b"))
