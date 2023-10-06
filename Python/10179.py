# Coupons 
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    price = float(sys.stdin.readline().rstrip())
    print("$", end="")
    print("%.2f" % (round(price * 80 / 100, 2)))
