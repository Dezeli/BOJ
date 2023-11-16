# 뱀과 사다리 게임
from sys import stdin
from collections import defaultdict, deque

N, M = map(int, stdin.readline().split(" "))
move = defaultdict(int)
check = [0 for _ in range(101)]

for i in range(1, 101):
    move[i] = i
for _ in range(N+M):
    x, y = map(int, stdin.readline().split(" "))
    move[x] = y

queue = deque()
queue.append([1, 0])
while queue:
    cur, time = queue.popleft()
    if cur== 100:
        print(time)
        break
    elif cur>100:
        continue
    if check[cur]==1:
        continue
    check[cur] = 1
    queue += [[move[cur+1], time +1], [move[cur+2], time +1], [move[cur+3], time +1], [move[cur+4], time +1], [move[cur+5], time +1], [move[cur+6], time +1]]
