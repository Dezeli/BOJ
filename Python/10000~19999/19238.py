# 스타트 택시
import sys
from collections import deque

input = sys.stdin.readline

n, m, energy = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
startX, startY = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(startX, startY):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((startX, startY))
    visited[startX][startY] = 0

    while queue:
        popX, popY = queue.popleft()

        for i in range(4):
            nextX, nextY = popX + dx[i], popY + dy[i]

            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= n:
                continue
            if road[nextX][nextY] == 1 or visited[nextX][nextY] != -1:
                continue

            visited[nextX][nextY] = visited[popX][popY] + 1
            queue.append((nextX, nextY))

    return visited


def check_dist(visited: list, people: list):
    i = 0
    for px, py, ax, ay in people:
        people[i].append(visited[px - 1][py - 1])
        i += 1

    people.sort(key=lambda x: (-x[4], -x[0], -x[1]))


def solve(startX, startY):
    global energy
    while people:
        visitied = bfs(startX - 1, startY - 1)
        check_dist(visitied, people)
        px, py, ax, ay, dist = people.pop()

        for temp in people:
            temp.pop()

        visitied = bfs(px - 1, py - 1)
        dist2 = visitied[ax - 1][ay - 1]
        startX, startY = ax, ay

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        energy -= dist
        if energy < 0:
            break

        energy -= dist2
        if energy < 0:
            break

        energy += dist2 * 2

    if energy < 0:
        print(-1)
    else:
        print(energy)


solve(startX, startY)