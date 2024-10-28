# 쉬운 계단 수

N = int(input())

stairs = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    stairs[0][i] = 1

for i in range(1, N):
    stairs[i][0] = stairs[i - 1][1]
    stairs[i][9] = stairs[i - 1][8]
    for j in range(1, 9):
        stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]

print(sum(stairs[N - 1]) % 1000000000)
