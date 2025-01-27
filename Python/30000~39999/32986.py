# 나는 건포도가 싫어요
import sys

input = sys.stdin.readline

X, Y, Z = map(int, input().split())
if X == Y == Z == 3:
    print(0)
else:
    small = min(X, Y, Z)
    if small % 2 == 1:
        print(small // 2)
    else:
        print(small // 2 - 1)
