# 이진수 덧셈
import sys

num1, num2 = map(str, sys.stdin.readline().split())
print(format(int(format(int(num1, 2), "d")) + int(format(int(num2, 2), "d")), "b"))
