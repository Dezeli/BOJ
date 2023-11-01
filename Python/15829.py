# Hashing
import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline()

val = 0

for i in range(L):
    val += (ord(string[i])-96)*(31**i)

print(val%1234567891)