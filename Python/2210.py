# 숫자판 점프
import sys

input = sys.stdin.readline

num_board = [list(input().rstrip().split()) for _ in range(5)]

num_set = set()

def make_num(num, x, y):
    if len(num)==6:
        num_set.add(num)
        return
    
    if x<0 or x>=5:
        return
    if y<0 or y>=5:
        return

    make_num(num+num_board[x][y], x+1, y)
    make_num(num+num_board[x][y], x-1, y)
    make_num(num+num_board[x][y], x, y+1)
    make_num(num+num_board[x][y], x, y-1)

for i in range(5):
    for j in range(5):
        make_num('', i, j)


print(len(num_set))