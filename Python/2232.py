# 지뢰
import sys

input = sys.stdin.readline

N = int(input())
bombs = [0]

max_bomb = 0
for _ in range(N):
    b = int(input())
    bombs.append(b)
    max_bomb = max(max_bomb, b)

idxs = []
while sum(bombs)>0:
    try:
        i = bombs.index(max_bomb)
    except:
        max_bomb -= 1
        continue
    
    idxs.append(i)
    lefti = i
    righti = i
    while True:
        if lefti < 1:
            break
        if bombs[lefti-1] < bombs[lefti]:
            lefti -= 1
        else:
            break
    while True:
        if righti > N-1:
            break
        if bombs[righti] > bombs[righti+1]:
            righti += 1
        else:
            break
    
    for i in range(lefti, righti+1):
        bombs[i] = 0

idxs.sort()
for i in idxs:
    print(i)