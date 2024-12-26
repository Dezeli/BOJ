# Router
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
router = deque()

while True:
    d = int(input())
    if d==-1:
        break
    if d==0:
        router.popleft()
    else:
        if len(router)>=N:
            continue
        else:
            router.append(d)
if router:
    print(*router)
else:
    print("empty")