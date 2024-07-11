# 해변
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = [input().rstrip() for _ in range(N)]

beach = 0

for i in range(N):
    for j in range(M-1):
        if data[i][j] != data[i][j+1]:
            beach += 1
    
    if i==N-1:
        continue
    if i%2==0:
        if data[i][0] != data[i+1][0]:
            beach += 1
        for j in range(1, M):
            if data[i][j] != data[i+1][j]:
                beach += 1
            if data[i][j] != data[i+1][j-1]:
                beach += 1
    else:
        if data[i][M-1] != data[i+1][M-1]:
            beach += 1
        for j in range(M-1):
            if data[i][j] != data[i+1][j]:
                beach += 1
            if data[i][j] != data[i+1][j+1]:
                beach += 1
print(beach)