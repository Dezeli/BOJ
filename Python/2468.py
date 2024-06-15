# 안전 영역
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < N) and (0 <= ny < N) and not sink[nx][ny] and H[nx][ny] > h:
            sink[nx][ny] = True
            dfs(nx, ny, h)


N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for k in range(max(map(max, H))):
    sink = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if H[i][j] > k and not sink[i][j]:
                cnt += 1
                sink[i][j] = True
                dfs(i, j, k)
    ans = max(ans, cnt)

print(ans)
