# 키로거
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().rstrip()
    l = deque([])
    r = deque([])
    for i in S:
        if l and i == '-':
            l.pop()
        elif l and i == '<':
            r.appendleft(l.pop())
        elif r and i == '>':
            l.append(r.popleft())
        elif i != '<' and i != '>' and i != '-':
            l.append(i)

    print(''.join(l + r))