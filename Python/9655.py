# 돌 게임
import sys

input = sys.stdin.readline

N = int(input())

win = [False for _ in range(1001)]
win[1] = True
win[3] = True

for i in range(5, N+1):
    if win[i-1]==1 or win[i-3]==1:
        win[i] = False
    else:
        win[i] = True

if win[N]:
    print("SK")
else:
    print("CY")
