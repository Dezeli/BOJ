# 그림
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

cnt_p = 0
max_p = 0


def search(a, b):
    global area

    if a >= n or b >= m:
        return
    if a < 0 or b < 0:
        return
    if paper[a][b] == 0:
        return
    if visit[a][b] == 1:
        return
    visit[a][b] = 1

    area += 1
    search(a + 1, b)
    search(a - 1, b)
    search(a, b + 1)
    search(a, b - 1)


for i in range(n):
    for j in range(m):
        area = 0
        search(i, j)
        if area > 0:
            cnt_p += 1
            max_p = max(area, max_p)

print(cnt_p)
print(max_p)
