# 파이프 옮기기 1
import sys
import copy

input = sys.stdin.readline

N = int(input())
pipe_map = []

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    pipe_map.append(line)

print(map)

def move(pipe, dir):
    print(pipe)
    if pipe[-1] == [N-1, N-1]:
        print(111)
        return 1
    
    if dir == "diagonal":
        for i, j in pipe:
            if i<0 or i>=N:
                return 0
            if j<0 or j>=N:
                return 0
            if map[i][j]:
                return 0
        if map[i-1][j]:
            return 0
        if map[i][j]=="1":
            return 0
    else:
        for i, j in pipe:
            if i<0 or i>=N:
                return 0
            if j<0 or j>=N:
                return 0
            if map[i][j]=="1":
                print(map[i][j])
                print("123123")
                return 0

    print("111111111111")
    last_pipe = pipe[-1]
    horizontal_pipe = copy.deepcopy(last_pipe)
    horizontal_pipe[1] += 1
    verticle_pipe = copy.deepcopy(last_pipe)
    verticle_pipe[0] += 1
    diagonal_pipe = copy.deepcopy(last_pipe)
    diagonal_pipe[0] += 1
    diagonal_pipe[1] += 1

    if dir=="horizontal":
        return move([last_pipe, horizontal_pipe], "horizontal") + move([last_pipe, diagonal_pipe], "diagonal")
    elif dir=="vertical":
        return move([last_pipe, verticle_pipe], "verticle") + move([last_pipe, diagonal_pipe], "diagonal")
    elif dir=="diagonal":
        return move([last_pipe, horizontal_pipe], "horizontal") + move([last_pipe, verticle_pipe], "verticle") + move([last_pipe, diagonal_pipe], "diagonal")
    


print(move([[0, 0], [0, 1]], "horizontal"))

