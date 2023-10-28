# Congruent Numbers
import sys

p1, q1, p2, q2 = map(int, sys.stdin.readline().split())
area = p1 * p2 / q1 / q2 / 2
if area == int(area):
    print(1)
else:
    print(0)
