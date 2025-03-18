# 전구와 스위치
import sys

input = sys.stdin.readline

N = int(input())

start = [int(i) for i in input().rstrip()]
end = [int(i) for i in input().rstrip()]


res1 = 1
b1 = start[:]
b1[0] = 1 - b1[0]
b1[1] = 1 - b1[1]

for i in range(1, N):
    if b1[i-1] != end[i-1]:
        for j in range(i-1, i+2):
            if j < N:
                b1[j] = 1 - b1[j]
        res1 += 1

for i in range(N):
    if b1[i] != end[i]:
        res1 = -1

res2 = 0
for i in range(1, N):
    if start[i - 1] != end[i - 1]:
        for j in range(i - 1, i + 2):
            if j < N:
                start[j] = 1 - start[j]
        res2 += 1

for i in range(N):
    if start[i] != end[i]:
        res2 = -1

if res1 != -1 and res2 != -1:
    print(min(res1, res2))
elif res1 != -1:
    print(res1)
else:
    print(res2)
