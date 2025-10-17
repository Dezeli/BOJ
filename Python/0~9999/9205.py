# 맥주 마시면서 걸어가기
import sys

input= sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    move = [list(map(int, input().split()))]
    store = [list(map(int, input().split())) for _ in range(n+1)]
    visit = [0]*(n+1)

    while move:
        x1, y1 = move.pop()
        for i in range(n+1):
            if visit[i]:
                continue
            x2, y2 = store[i]
            if abs(x1-x2)+abs(y1-y2)<=1000:
                visit[i] = 1
                move.append([x2, y2])
    if visit[-1]:
        print("happy")
    else:
        print("sad")
    

