# Pizza
import math

n = int(input())

for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())

    slice = A1/P1
    whole = R1**2*math.pi/P2

    if slice>whole:
        print("Slice of pizza")
    else:
        print("Whole pizza")