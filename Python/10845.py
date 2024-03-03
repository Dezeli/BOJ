# 큐
import sys

N = int(sys.stdin.readline().rstrip())
quene = []

for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if order == "front":
        if quene:
            print(quene[0])
        else:
            print(-1)
    elif order == "back":
        if quene:
            print(quene[-1])
        else:
            print(-1)
    elif order == "size":
        print(len(quene))
    elif order == "empty":
        if quene:
            print(0)
        else:
            print(1)
    elif order == "pop":
        if quene:
            print(quene.pop(0))
        else:
            print("-1")
    else:
        quene.append(order.split(" ")[1])
