# 벽 부수고 이동하기 2
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [input().rstrip() for _ in range(N)]


def wall_check(i, j):
    if not (0<=i<N):
        return -1
    if not (0<=j<M):
        return -1
    
    if board[i][j]=='1':
        return 1
    else:
        return 0

min_arrive = 1e9
move = [[0, 0, 1, 0]]
while move:
    i, j, m, b = move.pop()
    if b > K:
        continue
    if i==N-1 and j==M-1:
        min_arrive = min(min_arrive, m)
        continue
    
    u = wall_check(i-1, j)
    if u!=-1:
        move.append([i-1, j, m+1, b+u])
    d = wall_check(i+1, j)
    if d!=-1:
        move.append([i+1, j, m+1, b+d])
    l = wall_check(i, j-1)
    if l!=-1:
        move.append([i, j-1, m+1, b+l])
    r = wall_check(i, j+1)
    if r!=-1:
        move.append([i, j+1, m+1, b+r])
