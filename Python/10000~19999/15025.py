# Judging Moose
import sys

A, B = map(int, sys.stdin.readline().split())
if A == B:
    if A == 0:
        print("Not a moose")
    else:
        print(f"Even {A+B}")
else:
    print(f"Odd {max([A,B])*2}")
