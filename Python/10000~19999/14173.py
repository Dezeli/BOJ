# Square Pasture
import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

lx = min([x1, x3])
rx = max([x2, x4])
ly = min([y1, y3])
ry = max([y2, y4])
print(max(abs(lx - rx), abs(ly - ry)) ** 2)
