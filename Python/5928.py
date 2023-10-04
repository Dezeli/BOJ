# Contest Timing
import sys

D, H, M = map(int, sys.stdin.readline().split())
time = M - 11 + (H - 11) * 60 + (D - 11) * 1440
if time < 0:
    print(-1)
else:
    print(time)
