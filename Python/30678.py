# 별 안에 별 안에 별 찍기
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

len_line = 5**N
stars = [[' ']*(len_line) for _ in range(len_line)]

shape = [[1, 3], [2, 3], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4], [5, 2], [5, 4]]

def draw_stars(x, y, size):
    if size == 1:
        stars[x-1][y-1] = '*'
        return

    for i, j in shape:
        next_x = x-size + size//5*i
        next_y = y-size + size//5*j
        draw_stars(next_x, next_y, size//5)


draw_stars(len_line, len_line, len_line)

for line in stars:
    print(''.join(line))