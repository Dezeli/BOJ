# 에디터
import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()
queue = deque([i for i in S])
idx = len(S)

M = int(input())

for _ in range(M):
    ins = input().rstrip()
    if ins=='L':
        if idx!=0:
            idx -= 1
            queue.appendleft(queue.pop())
    elif ins=='D':
        if idx!=len(queue):
            idx += 1
            queue.append(queue.popleft())
    elif ins=='B':
        if idx!=0:
            queue.pop()
            idx -= 1
    else:
        ins, s = ins.split()
        queue.append(s)
        idx += 1

while idx < len(queue):
    queue.append(queue.popleft())
    idx += 1
print(''.join(queue))
