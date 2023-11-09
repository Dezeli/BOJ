# 헌내기는 친구가 필요해
import sys

N, M = map(int, sys.stdin.readline().split(" "))

map = []
for y in range(N):
    line = list(sys.stdin.readline().rstrip())
    if 'I' in line:
        root = [line.index('I'), y]
    map.append(line)

def check(root):
    stack = [root]
    point = 0
    while stack:
        x, y = stack.pop()
        if x<0 or y<0 or x>=M or y>=N:
            continue
        if map[y][x]=='O' or map[y][x]=='I':
            map[y][x] = 'X'
            stack.append([x+1, y])
            stack.append([x-1, y])
            stack.append([x, y+1])
            stack.append([x, y-1])
        elif map[y][x]=='P':
            map[y][x] = 'X'
            point += 1
            stack.append([x+1, y])
            stack.append([x-1, y])
            stack.append([x, y+1])
            stack.append([x, y-1])

    return point


point = check(root)
if point:
    print(point)
else:
    print("TT")