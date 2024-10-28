# 내려가기
import sys

input = sys.stdin.readline

N = int(input())
max_table = [0, 0, 0]
min_table = [0, 0, 0]
for _ in range(N):
    line = list(map(int, input().split(" ")))
    max_line = [line[0] + max_table[0], line[1] + max_table[1], line[2] + max_table[2]]
    max_table = [max(max_line[:2]), max(max_line), max(max_line[1:])]
    min_line = [line[0] + min_table[0], line[1] + min_table[1], line[2] + min_table[2]]
    min_table = [min(min_line[:2]), min(min_line), min(min_line[1:])]

print(max(max_line), min(min_line))
