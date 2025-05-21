from collections import deque

N, M, T = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]
# 동 - 서 - 남 - 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def rotate(x, d, k):
    q = deque()
    q.extend(plate[x])
    if d == 0:
        q.rotate(k)
    else:
        q.rotate(-k)
    plate[x] = list(q)


def change_avg():
    avg_cnt = 0
    all_sum = 0
    for i in range(N):
        for j in range(M):
            if plate[i][j] != 0:
                avg_cnt += 1
                all_sum += plate[i][j]
    if avg_cnt == 0:
        return False
    avg = all_sum / avg_cnt
    for i in range(N):
        for j in range(M):
            if plate[i][j] != 0:
                if plate[i][j] > avg:
                    plate[i][j] -= 1
                elif plate[i][j] < avg:
                    plate[i][j] += 1
    return True

def solve(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    value = plate[x][y]
    plate[x][y] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= M:
                if y == 0:
                    ny = M-1
                elif y == M-1:
                    ny = 0
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny]:
                    if plate[nx][ny] == value:
                        cnt += 1
                        plate[nx][ny] = 0
                        visit[nx][ny] = True
                        q.append((nx, ny))
    if cnt == 0:
        plate[x][y] = value
    return cnt


for _ in range(T):
    x, d, k = map(int, input().split())
    check_sum = 0
    for i in range(N):
        check_sum += sum(plate[i])
        if (i+1) % x == 0:
            rotate(i, d, k)
    if check_sum == 0:
        break
    else:
        visit = [[False] * M for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not visit[i][j] and plate[i][j] != 0:
                    cnt += solve(i, j)
        if cnt == 0:
            change_avg()

ans = 0
for i in range(N):
    ans += sum(plate[i])

print(ans)