# 벽 부수고 이동하기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

minimap = []

for _ in range(N):
    minimap.append(input())


def move():
    check_item = [[False]*M for _ in range(N)]
    check_notem = [[False]*M for _ in range(N)]

    move_que = [[[0, 0], True]]
    
    cnt_move = 0
    while True:
        cnt_move += 1
        next_move_que = []
        while move_que:
            pos, item = move_que.pop()

            y, x = pos[0], pos[1]

            if y<0 or y>=N:
                continue
            if x<0 or x>=M:
                continue
            
            if y==N-1 and x==M-1:
                return cnt_move
            
            if item:
                if check_item[y][x]:
                    continue
            else:
                if check_notem[y][x]:
                    continue
            if not item and minimap[y][x]=="1":
                continue
            
            if item and minimap[y][x]=="1":
                next_move_que += [[[y-1, x], False], [[y+1, x], False], [[y, x-1], False], [[y, x+1], False]]
                check_notem[y][x] = True
            else:
                next_move_que += [[[y-1, x], item], [[y+1, x], item], [[y, x-1], item], [[y, x+1], item]]
                if item:
                    check_item[y][x] = True
                else:
                    check_notem[y][x] = True
        if not next_move_que:
            return -1
        move_que += next_move_que


print(move())