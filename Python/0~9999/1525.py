# 퍼즐
import sys
from collections import deque

input = sys.stdin.readline
start = []
for _ in range(3):
    start += list(map(int, input().split()))
start = tuple(start)
end = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def swap(t, x, y):
    if x < 0 or x > 8 or y < 0 or y > 8:
        return None
    if (x==2 and y==3) or (x==3 and y==2) or (x==5 and y==6) or (x==6 and y==5):
        return None
    l = [i for i in t]
    l[x], l[y] = l[y], l[x]
    return tuple(l)

visit = set()
queue = deque([[start, 0]])
while queue:
    t, c = queue.popleft()
    if t in visit:
        continue
    visit.add(t)
    if t == end:
        print(c)
        break
    for i in range(9):
        if t[i]==0:
          up = swap(t, i, i-3)
          down = swap(t, i, i+3)
          left = swap(t, i, i-1)
          right = swap(t, i, i+1)
          if up and up not in visit:
              queue.append([up, c+1])
          if down and down not in visit:
              queue.append([down, c+1])
          if left and left not in visit:
              queue.append([left, c+1])
          if right and right not in visit:
              queue.append([right, c+1])
          break
if end not in visit:
    print(-1)