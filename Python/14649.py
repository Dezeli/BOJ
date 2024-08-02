# 문홍안
import sys

input = sys.stdin.readline

P = int(input())
N = int(input())

stones = [0 for _ in range(101)]

for _ in range(N):
    loc, dir = input().rstrip().split()

    if dir=='L':
        for i in range(1, int(loc)):
            stones[i] += 1
    else:
        for i in range(int(loc)+1, 101):
            stones[i] += 1


R = 0
G = 0
B = -1
for i in stones:
    if i%3==0:
        B += 1
    elif i%3==1:
        R += 1
    else:
        G += 1

print("{:.2f}".format(B/100*P))
print("{:.2f}".format(R/100*P))
print("{:.2f}".format(G/100*P))