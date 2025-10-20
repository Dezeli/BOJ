# 청소년 상어
import sys
import copy

input = sys.stdin.readline

# dir (0↗) 1↑ , 2↖, 3←, 4↙, 5↓, 6↘, 7→, 8↗
dx = [-1, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [1, 0, -1, -1, -1, 0, 1, 1, 1]

def fish_move(d2, fish):
    for n in range(1, 17):
        if fish[n]:
            i = fish[n][0]
            j = fish[n][1]
            dir = fish[n][2]
            for p in range(8):
                change_dir = (dir+p)%8
                x = i+dx[change_dir]
                y = j+dy[change_dir]
                if x<0 or y<0 or x>=4 or y>=4:
                    continue
                if d2[x][y]==-1:
                    continue
                elif d2[x][y]==0:
                    d2[x][y], d2[i][j] = d2[i][j], d2[x][y]
                    fish[n] = [x, y, change_dir]
                    break
                else:
                    d2[x][y], d2[i][j] = d2[i][j], d2[x][y]
                    fish[n] = [x, y, change_dir]
                    fish[d2[i][j]] = [i, j, fish[d2[i][j]][2]]
                    break

def shark_move(d2, fish):
    can_move = []

    i = fish[0][0]
    j = fish[0][1]
    dir = fish[0][2]
    for _ in range(3):
        i += dx[dir]
        j += dy[dir]
        if i<0 or j<0 or i>=4 or j>=4:
            continue
        if d2[i][j]==0:
            continue
        can_move.append([i, j, fish[d2[i][j]][2]])

    return can_move

def total_eat(fish):
    cnt = 0
    for i in range(1, 17):
        if not fish[i]:
            cnt += i
    return cnt

max_eat = 0
def backtrack(d2, fish):
    global max_eat
    fish_move(d2, fish)

    shark = shark_move(d2, fish)
    if not shark:
        eat = total_eat(fish)
        max_eat = max(max_eat, eat)
        return
    for i, j, dir in shark:
        new_d2 = copy.deepcopy(d2)
        new_fish = copy.deepcopy(fish)
        new_d2[new_fish[0][0]][new_fish[0][1]] = 0
        new_fish[new_d2[i][j]] = 0
        new_d2[i][j] = -1
        new_fish[0] = [i, j, dir]
        backtrack(new_d2, new_fish)



d2 = []
fish = [0]*17

for i in range(4):
    data = list(map(int, input().split()))
    d1 = []
    for j in range(4):
        fish_num = data[j*2]
        fish_dir = data[j*2+1]
        d1.append(fish_num)
        fish[fish_num] = [i, j, fish_dir]
    d2.append(d1)

fish[0] = [0, 0, fish[d2[0][0]][2]]
fish[d2[0][0]] = 0
d2[0][0] = -1

backtrack(d2, fish)
print(max_eat)

