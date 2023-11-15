# AC
from sys import stdin
from collections import deque

T = int(stdin.readline().rstrip())

for _ in range(T):
    p = stdin.readline().rstrip()
    d = p.count('D')
    n = int(stdin.readline().rstrip())

    if n < d:
        nums = stdin.readline()
        print("error")
        continue
    elif n == d:
        nums = stdin.readline()
        print("[]")
        continue
    
    
    queue = deque()
    nums = list(map(int, stdin.readline()[1:-2].split(",")))
    queue += nums
    rev = False
    for ord in p:
        if ord == 'R':
            rev = not rev
        else:
            if rev:
                queue.pop()
            else:
                queue.popleft()
    if rev:
        queue.reverse()
    print('[' + ','.join(str(i) for i in queue)+']')