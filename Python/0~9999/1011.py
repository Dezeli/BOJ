# Fly me to the Alpha Centauri
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    if (y-x)%2==0:
        mid = (y-x)//2
    else:
        mid = (y-x)//2 + 1
    i = 1
    move = 0
    while True:
        move += i
        if move >= mid:
            break
        i += 1
    
    for j in range(1, i):
        move += j
    if move >= y-x:
        print(i*2-1)
    else:
        print(i*2)

