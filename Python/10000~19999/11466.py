# Alex Origami Squares
import sys

xy = list(map(int, sys.stdin.readline().split()))
xy.sort()
if xy[0] * 3 / 2 >= xy[1]:
    print(xy[0] / 2)
elif xy[0] * 3 >= xy[1]:
    print(xy[1] / 3)
elif xy[0] * 3 < xy[1]:
    print(xy[0])
