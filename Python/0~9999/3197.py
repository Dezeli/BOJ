# 백조의 호수
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

lake = []
swans = []

for i in range(R):
    l = input().rstrip()
    for j in range(C):
        if l[j]=='L':
            swans.append([i, j])
    lake.append(l)

s1 = [swans[0]]
s2 = [swans[1]]
water = []