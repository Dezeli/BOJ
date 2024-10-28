# Beat the Spread!
import sys

plus, minus = map(int, sys.stdin.readline().split(" "))
if (plus + minus) % 2 != 0 or (plus - minus) % 2 != 0 or plus < minus:
    print(-1)
else:
    print((plus + minus) // 2, (plus - minus) // 2)
