# 덱
import sys

N = int(sys.stdin.readline().rstrip())
deque = []

for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if order == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif order == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif order == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif order == "pop_back":
        if deque:
            print(deque.pop(-1))
        else:
            print(-1)
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif order == "pop":
        if deque:
            print(deque.pop(0))
        else:
            print("-1")
    else:
        pos, num = order.split(" ")
        if pos[-1]=='t':
            deque.insert(0, num)
        else:
            deque.append(num)