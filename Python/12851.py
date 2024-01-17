# 숨바꼭질 2
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

INF = int(1e9)

short_time = [INF for _ in range(200001)]

moves = deque([[N, 0]])
while moves:
    move, time = deque.popleft(moves)

    if move == K:
        cnt = 1
        for new_move, new_time in moves:
            if time != new_time:
                break
            if new_move==K:
                cnt += 1
        break

    if short_time[move] >= time:
        short_time[move] = time
        if move >= 1:
            moves.append([move-1, time+1])
        if move < 100000:
            moves.append([move+1, time+1])
            moves.append([move*2, time+1])
    
print(time)
print(cnt)