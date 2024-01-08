# 별 찍기 - 18
import sys

input = sys.stdin.readline

N = int(input())
max_x = 2**(N+1)-3
max_y = 2**N-1

stars = [[' ']*(max_x) for _ in range(max_y)]

first_x = max_x//2
for i in range(1, N+1):
    if i == 1:
        first_y = 0
    if i%2==1:
        first_y *= 4
    else:
        first_y += 1

def draw_star(rec, N, vertex):
    if rec==N+1:
        return
    
    if rec==1:
        x, y = vertex
        stars[y][x] = "*"
        new_vertex = [x, y-1]
        draw_star(rec+1, N, new_vertex)
    else:
        if rec%2==1:
            dir = -1
        else:
            dir = 1

        mid_x, mid_y = vertex
        x_len = (2**(rec+1)-3)//2
        left_x = mid_x - x_len
        right_x = mid_x + x_len
        for x in range(left_x, right_x + 1):
            stars[mid_y][x] = "*"
        
        y = mid_y
        while left_x != right_x:
            left_x += 1
            right_x -= 1
            y += dir
            stars[y][left_x] = "*"
            stars[y][right_x] = "*"
        new_vertex = [mid_x, y+dir]
        draw_star(rec+1, N, new_vertex)


draw_star(1, N, [first_x, first_y])
for line in stars:
    print("".join(line).rstrip())