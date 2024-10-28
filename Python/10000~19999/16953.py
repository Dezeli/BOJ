# A → B
import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split(" "))

root = (A, 1)
check = deque([root])
able = False

while check:
    cur, time = check.popleft()
    time += 1
    A1 = cur * 2
    if A1 == B:
        print(time)
        able = True
        break
    elif A1 < B:
        check.append((A1, time))

    A2 = int(str(cur) + "1")
    if A2 == B:
        print(time)
        able = True
        break
    elif A2 < B:
        check.append((A2, time))

if not able:
    print(-1)
