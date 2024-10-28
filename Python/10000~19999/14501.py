# 퇴사
import sys

input = sys.stdin.readline

N = int(input())
money = [[0, 0] for _ in range(N)]

for i in range(N):
    T, P = map(int, input().split())
    money[i] = [T + i, P]
    for j in range(0, i):
        if money[j][0] <= i:
            money[i][1] = max(money[i][1], money[j][1] + P)
    if T + i > N:
        money[i][1] = 0

print(max([money[i][1] for i in range(N)]))
