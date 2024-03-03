# Bicycle

a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

bike1 = 0
bike2 = 0

if T <= 30:
    bike1 = a
else:
    bike1 = (a + (T - 30) * x) * 21 - a * 20
if T <= 45:
    bike2 = b
else:
    bike2 = (b + (T - 45) * y) * 21 - b * 20

print(bike1, bike2)
