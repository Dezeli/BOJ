# 열쇠
import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

T = int(input())

def move(a, b):
    global h, w, cnt
    if not (0<=a<h):
        return
    if not (0<=b<w):
        return
    if visit[a][b] == 1:
        return
    num = ord(buliding[a][b])
    if num==42:
        return
    elif 65<=num<=90:
        door[buliding[a][b]].append([a, b])
        return
    elif 97<=num<=122:
        find.append(buliding[a][b])
    elif num==36:
        cnt += 1
    visit[a][b] = 1
    move(a-1, b)
    move(a+1, b)
    move(a, b-1)
    move(a, b+1)

for _ in range(T):
    h, w = map(int, input().split())
    buliding = [input().rstrip() for __ in range(h)]
    visit = [[0]*w for __ in range(h)]
    door = defaultdict(list)
    find = []
    cnt = 0

    keys = input().rstrip()
    for i in keys:
        for j in range(h):
            buliding[j] = buliding[j].replace(i.upper(), ".")
    
    for i in range(h):
        move(i, 0)
        move(i, w-1)

    for i in range(w):
        move(0, i)
        move(h-1, i)

    while find:
        k = find.pop()
        for i in range(h):
            buliding[i] = buliding[i].replace(k.upper(), ".")
        for i, j in door[k.upper()]:
            move(i, j)

    print(cnt)