# 8진수 2진수
import sys

num_Octal = str(sys.stdin.readline().rstrip())
print(format(int(num_Octal, 8), "b"))
