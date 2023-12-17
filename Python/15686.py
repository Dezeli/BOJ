# 치킨 배달
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split(" "))

chicken = []
houses = []

for i in range(N):
    line = list(map(int, input().split(" ")))
    for j, space in enumerate(line):
        if space == 1:
            houses.append([i, j])
        elif space == 2:
            chicken.append([i, j])

chicken_com = combinations(chicken, M)

min_distances = sys.maxsize


for case in chicken_com:
    distances = 0
    for i1, j1 in houses:
        dis = sys.maxsize
        for i2, j2 in case:
            dis = min([abs(i1-i2) + abs(j1-j2), dis])
        if dis >= min_distances or distances >= min_distances:
            distances += dis
            break
        else:
            distances += dis

    min_distances = min([distances, min_distances])

print(min_distances)
