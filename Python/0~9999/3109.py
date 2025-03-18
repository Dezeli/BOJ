# 빵집
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

R, C = map(int, input().split())

roads = [[i for i in input().rstrip()] for _ in range(R)]
visit = [[0] * C for _ in range(R)]


def DFS(y, x):
    if y < 0 or y >= R:
        return False

    if visit[y][x] == 1:
        return False
    visit[y][x] = 1

    if x == C - 1:
        return True

    if roads[y][x] == "x":
        return False

    r1 = DFS(y - 1, x + 1)
    if r1:
        return True
    r2 = DFS(y, x + 1)
    if r2:
        return True
    r3 = DFS(y + 1, x + 1)
    if r3:
        return True
    return False


cnt = 0
for i in range(R):
    result = DFS(i, 0)
    if result:
        cnt += 1
print(cnt)
