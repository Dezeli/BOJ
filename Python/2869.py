# PUŽ 
import sys

A, B, V = map(int, (sys.stdin.readline().rstrip()).split(" "))
time = (V - A) // (A - B) + 2
if (V - A) % (A - B) == 0:
    time -= 1
print(time)
