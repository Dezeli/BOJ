# Last Factorial Digit
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    fac = 1
    for i in range(2, N + 1):
        fac *= i

    print(fac % 10)
