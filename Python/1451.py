# 직사각형으로 나누기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

p_square = [[0 for _ in range(M+1)]]

for _ in range(N):
    row = input().rstrip()
    p_row = [0]
    for i in range(1, M+1):
        p_row.append(int(row[i-1]) + p_square[-1][i] + p_row[-1] - p_square[-1][i-1])
    p_square.append(p_row)

max_s = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if i==N and j==M:
            continue
        elif i==N:
            for k in range(j+1, M):
                s1 = p_square[N][j]
                s2 = p_square[N][k] - s1
                s3 = p_square[N][M] - s1 - s2
                max_s = max(s1*s2*s3, max_s)
            for k in range(1, N):
                s1 = p_square[N][j]
                s2 = p_square[k][M] - p_square[k][j]
                s3 = p_square[N][M] - s1 - s2
                max_s = max(s1*s2*s3, max_s)
        elif j==M:
            for k in range(i+1, N):
                s1 = p_square[i][M]
                s2 = p_square[k][M] - s1
                s3 = p_square[N][M] - s1 - s2
                max_s = max(s1*s2*s3, max_s)
            for k in range(1, M):
                s1 = p_square[i][M]
                s2 = p_square[N][k] - p_square[i][k]
                s3 = p_square[N][M] - s1 - s2
                max_s = max(s1*s2*s3, max_s)
        else:
            s1 = p_square[i][j]
            s2 = p_square[i][M] - s1
            s3 = p_square[N][M] - s1 - s2
            max_s = max(s1*s2*s3, max_s)

            s2 = p_square[N][j] - s1 
            s3 = p_square[N][M] - s1 -s2
            max_s = max(s1*s2*s3, max_s)
            

print(max_s)