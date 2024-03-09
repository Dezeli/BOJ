# 숫자 정사각형

N, M = map(int, input().split())

square = []

for _ in range(N):
    line = input()
    square.append(line)

max_dots = 1

for i1 in range(N):
    for i2 in range(i1+1, N):
        for j1 in range(M):
            j2 = j1 + i2 - i1
            if j2>=M:
                continue
            if int(square[i1][j1]) == int(square[i1][j2]) == int(square[i2][j1]) == int(square[i2][j2]):
                max_dots = max(max_dots, (i2-i1+1)*(j2-j1+1))

print(max_dots)