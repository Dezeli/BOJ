# 순회강연
import sys

input = sys.stdin.readline

n = int(input())

lec = []
for _ in range(n):
    p, d = map(int, input().strip().split())
    lec.append((p, d))

lec.sort(reverse=True, key=lambda x: x[0])


days = set(range(1, 10001))

money = 0
for p, d in lec:
    for day in range(d, 0, -1):
        if day in days:
            days.remove(day)
            money += p
            break

print(money)
