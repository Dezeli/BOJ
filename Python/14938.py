# 서강그라운드
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

INF = int(1e9)
game_map = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    game_map[a][b] =  l
    game_map[b][a] = l

for i in range(1, n + 1):
    game_map[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            game_map[i][j] = min(game_map[i][j], game_map[i][k] + game_map[k][j])


max_item = 0
for i in range(1, n + 1):
    case_item = 0
    for j in range(1, n + 1):
        if game_map[i][j] <= m:
            case_item += items[j]
    max_item = max(max_item, case_item)

print(max_item)
