# 막대기
import sys

X = int(sys.stdin.readline().rstrip())

sticks = 0
while X != 0:
    X, stick = divmod(X, 2)
    sticks += stick

print(sticks)
