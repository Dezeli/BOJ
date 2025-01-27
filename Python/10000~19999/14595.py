# 동방 프로젝트 (Large)
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

villian = []
if M == 0:
    print(N)
else:
    for _ in range(M):
        x, y = map(int, input().split())
        villian.append([x, y])
    villian.sort(reverse=True)

    broke = []
    (
        x1,
        y1,
    ) = villian.pop()
    while villian:
        x2, y2 = villian.pop()
        if x2 <= y1:
            y1 = max(y1, y2)
        else:
            broke.append([x1, y1])
            x1, y1 = x2, y2
    broke.append([x1, y1])

    room = N
    for x, y in broke:
        room -= y - x
    print(room)
