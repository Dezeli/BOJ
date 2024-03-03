# 별 찍기 - 10
import sys

input = sys.stdin.readline

N = int(input())  # N = 3^k

stars = [[" "] * N for _ in range(N)]


def draw_star(i, j, size):
    if size == 3:
        for i in range(i - 2, i + 1):
            for j in range(j - 2, j + 1):
                stars[i][j] = "*"
        stars[i - 1][j - 1] = " "

    else:
        new_size = size // 3
        i1 = i - (new_size * 2)
        i2 = i - new_size
        i3 = i
        j1 = j - (new_size * 2)
        j2 = j - new_size
        j3 = j
        draw_star(i1, j1, new_size)
        draw_star(i1, j2, new_size)
        draw_star(i1, j3, new_size)
        draw_star(i2, j1, new_size)
        draw_star(i2, j3, new_size)
        draw_star(i3, j1, new_size)
        draw_star(i3, j2, new_size)
        draw_star(i3, j3, new_size)


draw_star(N - 1, N - 1, N)

for star in stars:
    print("".join(star))
