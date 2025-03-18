# 인구 이동
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())

people = []

for _ in range(N):
    r = list(map(int, input().split()))
    people.append(r)


def move(x, y):
    global p, finish
    if visit[x][y]:
        return

    visit[x][y] = 1
    p += people[x][y]
    c.append([x, y])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N:
            continue
        if L <= abs(people[x1][y1] - people[x][y]) <= R:
            finish = False
            move(x1, y1)


ans = 0
while True:
    finish = True
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p = 0
            c = []
            move(i, j)
            for x, y in c:
                people[x][y] = p // (len(c))

    if finish:
        break
    ans += 1

print(ans)
