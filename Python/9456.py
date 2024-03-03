# 스티커
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    line1 = list(map(int, sys.stdin.readline().split(" ")))
    line2 = list(map(int, sys.stdin.readline().split(" ")))

    zero = 0
    one = 0
    two = 0

    for i in range(n):
        zero, one, two = (
            max([one, two]),
            line1[i] + max([zero, two]),
            line2[i] + max([zero, one]),
        )

    print(max([zero, one, two]))
