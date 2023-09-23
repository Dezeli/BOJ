# 게임
import sys

X, Y = map(int, sys.stdin.readline().split())
if X == Y:
    print(-1)
else:
    per = int(100 * Y / X)
    newPer = int(100 * Y / X)
    if per + 1 == 100:
        print(-1)
    else:
        time = 0
        while newPer < per + 1:
            if int(100 * (Y + time + 1000000000) / (X + time + 1000000000)) < per + 1:
                time += 1000000000
            elif int(100 * (Y + time + 10000000) / (X + time + 10000000)) < per + 1:
                time += 10000000
            elif int(100 * (Y + time + 1000000) / (X + time + 1000000)) < per + 1:
                time += 1000000
            elif int(100 * (Y + time + 100000) / (X + time + 100000)) < per + 1:
                time += 100000
            elif int(100 * (Y + time + 10000) / (X + time + 10000)) < per + 1:
                time += 10000
            elif int(100 * (Y + time + 1000) / (X + time + 1000)) < per + 1:
                time += 1000
            elif int(100 * (Y + time + 100) / (X + time + 100)) < per + 1:
                time += 100
            elif int(100 * (Y + time + 10) / (X + time + 10)) < per + 1:
                time += 10
            else:
                time += 1
            newPer = int(100 * (Y + time) / (X + time))
        print(time)
