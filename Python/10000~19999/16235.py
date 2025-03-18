# 나무 재테크
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
ground = [[5] * N for _ in range(N)]

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

trees = [[[] for _ in range(N)] for _ in range(N)]
mid = set([])

for _ in range(M):
    x, y, k = map(int, input().split())
    mid.add((x - 1, y - 1))
    trees[x - 1][y - 1].append(k)

for i in mid:
    trees[i[0]][i[1]].sort()

for _ in range(K):
    fall = []
    for i in range(N):
        for j in range(N):
            dead = 0
            cur_trees = deque()
            for value in trees[i][j]:
                if value <= ground[i][j]:
                    ground[i][j] -= value
                    value += 1
                    if value % 5 == 0:
                        fall.append((i, j))
                    cur_trees.append(value)
                else:
                    dead += value // 2
            ground[i][j] += dead
            trees[i][j] = cur_trees

    while fall:
        x, y = fall.pop()
        for k in range(8):
            dx = dir[k][0] + x
            dy = dir[k][1] + y
            if 0 <= dx < N and 0 <= dy < N:
                trees[dx][dy].appendleft(1)

    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]


cnt = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            cnt += len(trees[i][j])
print(cnt)
