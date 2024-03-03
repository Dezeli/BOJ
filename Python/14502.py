# 연구소
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
ways = [[1, 0], [-1, 0], [0, 1], [0, -1]]
lab_map = []
blanks = []
first_bomb = []

for y in range(N):
    line = list(input().split())
    for x in range(M):
        if line[x] == "0":
            blanks.append([y, x])
        elif line[x] == "2":
            first_bomb.append([y, x])
    lab_map.append(line)

comb_blank = list(combinations(blanks, 3))

max_blank = 0
for change in comb_blank:
    len_blank = len(blanks)
    for y, x in change:
        lab_map[y][x] = "1"
        len_blank -= 1

    bomb = []
    for bomb_y, bomb_x in first_bomb:
        for i, j in ways:
            bomb.append([bomb_y + i, bomb_x + j])
    while bomb:
        bomb_y, bomb_x = bomb.pop()
        if bomb_y >= N or bomb_y < 0:
            continue
        if bomb_x >= M or bomb_x < 0:
            continue
        if lab_map[bomb_y][bomb_x] == "0":
            lab_map[bomb_y][bomb_x] = "2"
            len_blank -= 1
            if max_blank > len_blank:
                break
            for i, j in ways:
                bomb.append([bomb_y + i, bomb_x + j])

    max_blank = max([max_blank, len_blank])
    for y, x in blanks:
        lab_map[y][x] = "0"

print(max_blank)
