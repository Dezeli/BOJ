# 핸드폰 요금
import sys

N = int(sys.stdin.readline().rstrip())
callList = list(map(int, sys.stdin.readline().split()))
Y, M = 0, 0
for i in callList:
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15
if Y <= M:
    print("Y", end=" ")
if Y >= M:
    print("M", end=" ")
print(min([Y, M]))
