# 스타트링크
import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

move = deque([[0, S]])

visit = [F * 2] * (F + 1)

while move:
    c, f = move.popleft()

    if f < 1 or f > F:
        continue
    if visit[f] <= c:
        continue

    visit[f] = c
    if f == G:
        break

    move.append([c + 1, f + U])
    move.append([c + 1, f - D])


if visit[G] < F * 2:
    print(visit[G])
else:
    print("use the stairs")
