# 골드바흐의 추측
import sys

input = sys.stdin.readline

primes = [True] * 1000001

for i in range(2, int(len(primes) ** 0.5) + 1):
    if primes[i]:
        for j in range(2 * i, 1000001, i):
            primes[j] = False


while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(n - 3, 2, -2):
        if (primes[i] == True) and (primes[n - i] == True):
            print(f"{n} = {n-i} + {i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')
