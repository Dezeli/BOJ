# 사이클 게임
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
connection = [i for i in range(n+1)]
turn = 0

def find(x):
    if x == connection[x]:
        return x
    else:
        y = find(connection[x])
        connection[x] = y
        return y

def union(x, y, indx):
    global turn
    x = find(x)
    y = find(y)
    if x != y:
        connection[max(x, y)] = min(x,y)
    elif turn == 0:
        turn = indx

for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i + 1)

print(turn)