# Silnia

n = int(input())

fac = 1
for i in range(2, n + 1):
    fac *= i
    fac %= 10

print(fac)
