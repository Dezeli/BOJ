# 2×n 타일링 2
import sys

n = int(sys.stdin.readline().rstrip())

fac = [1, 1]
for i in range(2, 1500):
    fac.append(fac[-1]*i)

kinds = 0
for i in range(0, n+1, 2):
    short = n-i
    long = i//2
    kinds += fac[short+long]//(fac[short]*fac[long])*(2**(long))

print(kinds%10007)