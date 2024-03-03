# 덩치

N = int(input())

people = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

for a in people:
    bigger = 0
    for b in people:
        if a[0] < b[0] and a[1] < b[1]:
            bigger += 1
    print(bigger + 1, end=" ")
