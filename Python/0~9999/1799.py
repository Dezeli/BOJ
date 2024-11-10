# 비숍
import sys

input = sys.stdin.readline

N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
dia = [[[False] * (2 * N) for _ in range(2)] for _ in range(2)]

ans = [0, 0]
can = [[], []]
for i in range(N):
    for j in range(N):
        if chess[i][j] == 1:
            can[(i ^ j) & 1].append((i, j))

def backtrack(color, cur, cnt):
    if cur == len(can[color]):
        ans[color] = max(ans[color], cnt)
        return
    
    if cnt + len(can[color]) - cur <= ans[color]:
        return
    
    x, y = can[color][cur]
    if dia[color][0][x + y] or dia[color][1][x - y + N]:
        backtrack(color, cur + 1, cnt)
        return
    
    dia[color][0][x + y] = dia[color][1][x - y + N] = True
    backtrack(color, cur + 1, cnt + 1)
    dia[color][0][x + y] = dia[color][1][x - y + N] = False
    backtrack(color, cur + 1, cnt)

backtrack(0, 0, 0)
backtrack(1, 0, 0)

print(sum(ans))