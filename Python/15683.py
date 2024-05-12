# 감시
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

cctv = []
room = []
space = 0

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(M):
        if l[j]==0:
            space += 1
        if 0 < l[j] < 6:
            cctv.append([i, j])
    room.append(l)


def watch(i, j, num):
    if room[i][j] == 1:
        


