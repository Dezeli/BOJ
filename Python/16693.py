# Pizza Deal
import math

A1, P1 = map(int, input().split())
A2, P2 = map(int, input().split())


if A1/P1 > (A2**2)*math.pi/P2:
    print("Slice of pizza")
else:
    print("Whole pizza")