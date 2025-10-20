# 달이 차오른다, 가자.
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

d2 = []

bit2 = {'a':1, 'b':2, 'c':4, 'd':8, 'e':16, 'f':32}

move = deque([])
for i in range(N):
    d1 = input().rstrip()
    for j in range(M):
        if d1[j]=='0':
            move.append([0, 0, i, j])
    d2.append(d1)


visit = [[[0]*64 for _ in range(M)] for __ in range(N)]


def key_check(b, s):
    binary = format(b, '06b')
    if s=='A' and binary[5]=='1':
        return True
    if s=='B' and binary[4]=='1':
        return True
    if s=='C' and binary[3]=='1':
        return True
    if s=='D' and binary[2]=='1':
        return True
    if s=='E' and binary[1]=='1':
        return True
    if s=='F' and binary[0]=='1':
        return True
    return False

moon = False
while move:
    b, c, i, j = move.popleft()

    if i<0 or j<0 or i>=N or j>=M:
        continue
    if visit[i][j][b]:
        continue
    if d2[i][j]=='#':
        continue

    if d2[i][j]=='1':
        moon = True
        ans = c
        break

    if 64<ord(d2[i][j])<91:
        key = key_check(b, d2[i][j])
        if not key:
            continue
    elif 96<ord(d2[i][j])<123:
        if not key_check(b, d2[i][j].upper()):
            b += bit2[d2[i][j]]
    visit[i][j][b] = 1

    move.append([b, c+1, i+1, j])
    move.append([b, c+1, i-1, j])
    move.append([b, c+1, i, j+1])
    move.append([b, c+1, i, j-1])

if moon:
    print(ans)
else:
    print(-1)
