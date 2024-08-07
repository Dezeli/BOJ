# 세상은 하나의 손수건
import sys

input = sys.stdin.readline

N, finT = map(int, input().split())

x = 0
y = 0
lastT = 0
lastS = [1, 0]
for _ in range(N):
    T, S = input().rstrip().split()
    T = int(T)

    x += lastS[0] * (T - lastT)
    y += lastS[1] * (T - lastT)

    lastT = T
    if lastS[0] == 1:
        if S == "left":
            lastS = [0, 1]
        else:
            lastS = [0, -1]
    elif lastS[0] == -1:
        if S == "left":
            lastS = [0, -1]
        else:
            lastS = [0, 1]
    else:
        if lastS[1] == 1:
            if S == "left":
                lastS = [-1, 0]
            else:
                lastS = [1, 0]
        else:
            if S == "left":
                lastS = [1, 0]
            else:
                lastS = [-1, 0]

x += lastS[0] * (finT - lastT)
y += lastS[1] * (finT - lastT)

print(x, y)
