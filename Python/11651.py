# 좌표 정렬하기 2

N = int(input())

dots = []

for _ in range(N):
    dot = list(map(int, input().split()))
    dots.append(dot)

dots = sorted(dots, key=lambda x: (x[1], x[0]))
for dot in dots:
    print(dot[0], dot[1])
