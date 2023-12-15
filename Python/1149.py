# RGB거리
import sys

N = int(sys.stdin.readline().rstrip())
lastR = 0
lastG = 0
lastB = 0

for _ in range(N):
    R, G, B = map(int, sys.stdin.readline().split(" "))
    nextR = min([lastG, lastB]) + R
    nextG = min([lastR, lastB]) + G
    nextB = min([lastR, lastG]) + B

    lastR, lastG, lastB = nextR, nextG, nextB

print(min([lastR, lastG, lastB]))