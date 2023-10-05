# Don’t pass me the ball!
import sys

J = int(sys.stdin.readline().rstrip())
if J < 4:
    print("0")
else:
    print((J - 1) * (J - 2) * (J - 3) // 6)
