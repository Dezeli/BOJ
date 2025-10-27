# 볼록 껍질
import sys

input = sys.stdin.readline

N = int(input())
dots  = [list(map(int, input().split())) for _ in range(N)]

dots.sort(key=lambda p: (p[0], p[1]))

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

lower = []
for p in dots:
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

upper = []
for p in reversed(dots):
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)

outside_dots = lower + upper

print(len(outside_dots)-2)