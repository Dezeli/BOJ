# 체스판 다시 칠하기 2
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = []
for _ in range(N):
    line = input().rstrip()
    board.append(line)

c_sum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i+j)%2==0:
            if board[i-1][j-1] == 'B':
                c_sum[i][j] = c_sum[i-1][j]+c_sum[i][j-1]-c_sum[i-1][j-1]
            else:
                c_sum[i][j] = c_sum[i-1][j]+c_sum[i][j-1]-c_sum[i-1][j-1]+1
        else:
            if board[i-1][j-1] == 'W':
                c_sum[i][j] = c_sum[i-1][j]+c_sum[i][j-1]-c_sum[i-1][j-1]
            else:
                c_sum[i][j] = c_sum[i-1][j] + c_sum[i][j-1]-c_sum[i-1][j-1]+1

max_c = -2000**2
min_c = 2000**2
for i in range(K, N+1):
    for j in range(K, M+1):
        max_c = max(c_sum[i][j] - c_sum[i-K][j] - c_sum[i][j-K] + c_sum[i-K][j-K], max_c)
        min_c = min(c_sum[i][j] - c_sum[i-K][j] - c_sum[i][j-K] + c_sum[i-K][j-K], min_c)

print(min(min_c, max_c, K*K - min_c, K*K - max_c))