# ICONS

N = int(input())

a = 1
b = 1
while True:
    if a * b >= N:
        break
    if a > b:
        b += 1
    else:
        a += 1
print(a, b)
