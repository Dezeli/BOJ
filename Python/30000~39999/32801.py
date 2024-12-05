# Generalized FizzBuzz

n, a, b = map(int, input().split())

fizz, buzz, fibu = 0, 0, 0
for i in range(1, n + 1):
    if i % a == 0 and i % b == 0:
        fibu += 1
    elif i % a == 0:
        fizz += 1
    elif i % b == 0:
        buzz += 1

print(fizz, buzz, fibu)
