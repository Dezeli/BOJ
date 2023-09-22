# 유기농 배추
import sys

T = int(sys.stdin.readline().rstrip())
sys.setrecursionlimit(10**6)

for _ in range(T):
    farm = []
    M, N, K = map(int, sys.stdin.readline().split())
    for __ in range(N):
        farm.append([0] * M)
    for __ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        farm[Y][X] = 1
    wormNum = 0

    def erase(x, y):
        if x <= -1 or x >= M or y <= -1 or y >= N:
            return
        if farm[y][x] == 1:
            farm[y][x] = 0
        else:
            return
        erase(x - 1, y)
        erase(x + 1, y)
        erase(x, y - 1)
        erase(x, y + 1)

    for m in range(M):
        for n in range(N):
            if farm[n][m] == 1:
                wormNum += 1
                erase(m, n)
    print(wormNum)
