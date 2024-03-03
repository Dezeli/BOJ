# 별 찍기 - 11
import sys

input = sys.stdin.readline
N = int(input())  # N = 3 x 2^k

stars = [[" "] * 2 * N for _ in range(N)]


def draw_star(i, j, size):
    if size == 3:
        stars[i][j] = "*"
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"

    else:
        new_size = size // 2
        draw_star(i, j, new_size)
        draw_star(i + new_size, j - new_size, new_size)
        draw_star(i + new_size, j + new_size, new_size)


draw_star(0, N - 1, N)
for star in stars:
    print("".join(star))
