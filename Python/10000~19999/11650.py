# 좌표 정렬하기

N = int(input())

dots = []

for _ in range(N):
    dot = list(map(int, input().split()))
    dots.append(dot)

dots.sort()
for dot in dots:
    print(dot[0], dot[1])
