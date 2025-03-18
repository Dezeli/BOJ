# 배
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
boxes = deque(boxes)

if cranes[0] < boxes[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        cnt += 1
        next_boxes = deque([])
        i = 0
        while boxes and i < N:
            b = boxes.popleft()
            if cranes[i] >= b:
                i += 1
            else:
                next_boxes.append(b)
        boxes = next_boxes + boxes
    print(cnt)
