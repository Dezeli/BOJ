# 이모티콘
import sys
from collections import deque

input = sys.stdin.readline

S = int(input())

queue = deque([[1, 0, 0]])

visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True

while queue:
    s, c, cnt = queue.popleft()

    if s == S:
        print(cnt)
        break

    for i in range(3):
        if i == 0:
            newC, newS = s, s
        elif i == 1:
            newS, newC= s + c, c
        else:
            newS, newC = s - 1, c

        if newS>=1001 or newS<0 or newC>=1001 or newC<0 or visited[newS][newC]:
            continue

        visited[newS][newC] = True
        queue.append([newS, newC, cnt+1])