# 뒤집힌 덧셈
import sys

X, Y = sys.stdin.readline().split()
print(int(str(int(X[::-1]) + int(Y[::-1]))[::-1]))
